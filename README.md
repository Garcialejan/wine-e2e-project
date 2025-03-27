# ML wine-e2e-project

### Workflows--ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation-- Feature Engineering, Data Preprocessing...
4. Model Trainer
5. Model Evaluation- MLFLOW,Dagshub

## Workflows

1. Update config.yaml: configurations that we required for the data pipeline(credentiales for DB, ...) 
2. Update schema.yaml: schema of the data. Used for the data validation
3. Update params.yaml: params of the ML model or another requisites
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py