#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'CONTRACT.md', 'PUBLIC-EVIDENCE.md', 'EVIDENCE-REGISTRY.md',
    'BASELINE.md', 'MIGRATION.md', 'system-observations/README.md',
    'vsm-projections/README.md', 'comparison-cells/README.md', 'baselines/README.md',
    'frontier/README.md', 'historical/README.md',
]
errors = []
for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f'missing required file: {rel}')

for rel in ('README.md', 'CONTRACT.md', 'PUBLIC-EVIDENCE.md', 'BASELINE.md'):
    path = ROOT / rel
    if path.is_file() and 'experimental' not in path.read_text(encoding='utf-8').lower():
        errors.append(f'{rel}: must explicitly state experimental status')

contract = (ROOT / 'CONTRACT.md').read_text(encoding='utf-8') if (ROOT / 'CONTRACT.md').is_file() else ''
for phrase in (
    'general functional capability', 'domain-specific assessment', 'vsm-harness-profile',
    'vsm-harness-index', 'does not run or reproduce benchmark experiments',
):
    if phrase.lower() not in contract.lower():
        errors.append(f'CONTRACT.md: missing contract phrase: {phrase}')

if (ROOT / 'domain-projections').exists():
    errors.append('domain-projections/: domain-specific assessment is outside this repository boundary')

active_files = [
    ROOT / 'baselines' / 'FUNCTION-BASELINES.md',
    ROOT / 'baselines' / 'PRIMARY-BASELINES.md',
    ROOT / 'baselines' / 'S1-BASELINE.md',
    ROOT / 'frontier' / 'EVIDENCE-FRONTIER.md',
]
forbidden = {
    'domain_projection': 'active general layer must not own domain-specific projection state',
    '## Applied-domain projections': 'active general layer must not publish domain-specific projection sections',
    'Opensiro-operated runs are optional': 'active evidence contract forbids operated runs as evidence admission',
    's2-system-benchmarks/': 'old Index-local path leaked into active extracted view',
    's3-system-benchmarks/': 'old Index-local path leaked into active extracted view',
    's3star-system-benchmarks/': 'old Index-local path leaked into active extracted view',
    's4-system-benchmarks/': 'old Index-local path leaked into active extracted view',
    's5-system-benchmarks/': 'old Index-local path leaked into active extracted view',
}
for path in active_files:
    if not path.is_file():
        continue
    text = path.read_text(encoding='utf-8')
    for needle, why in forbidden.items():
        if needle in text:
            errors.append(f'{path.relative_to(ROOT)}: {why}: {needle}')

selection_path = ROOT / 'baselines' / 'primary-baselines.json'
if selection_path.is_file():
    data = json.loads(selection_path.read_text(encoding='utf-8'))
    if 'domains' in data.get('functions', {}).get('S1', {}):
        errors.append('baselines/primary-baselines.json: domain-specific derived state remains in active general layer')

registry = ROOT / 'system-observations' / 'registry.psv'
if registry.is_file():
    rows = [line for line in registry.read_text(encoding='utf-8').splitlines()[1:] if line.strip()]
    ids = [line.split('|', 1)[0] for line in rows]
    if len(ids) != 53 or len(set(ids)) != 53:
        errors.append(f'system-observations/registry.psv: expected 53 unique migrated observation IDs, got {len(set(ids))}/{len(ids)}')

tracked = subprocess.run(
    ['git', 'ls-files'], cwd=ROOT, text=True, capture_output=True
)
if tracked.returncode:
    errors.append(f'git ls-files failed: {tracked.stderr}')
else:
    generated_python = [
        path for path in tracked.stdout.splitlines()
        if '/__pycache__/' in f'/{path}' or path.endswith(('.pyc', '.pyo'))
    ]
    if generated_python:
        errors.append('generated Python cache must not be tracked: ' + ', '.join(generated_python))

for cmd in (
    [sys.executable, str(ROOT / 'system-observations' / 'validate.py')],
    [sys.executable, str(ROOT / 'system-observations' / 'render_registry.py'), '--check'],
):
    if Path(cmd[1]).is_file():
        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
        if result.returncode:
            errors.append(f"{' '.join(cmd)} failed:\n{result.stdout}{result.stderr}")

if errors:
    print('repository validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)
print('repository validation passed')
