# Make sure prodigy.json has appropriate environment variables
python scripts/mkconfig.py

# Show the stats, just for the logs
python -m prodigy stats

# Start Prodigy
python -m prodigy fix-json-outputs fix_json_outputs_001 annotation_results_to_fix_5000.jsonl -F json_editing_recipe.py
