## CMS

To run the application locally we need to run migration
 - we need to postgres / mysql running
 - create a database (for example cms)
 - `export APP_SETTINGS="config.DevelopmentConfig"`
 - `export DATABASE_URL="postgresql://localhost/cms"`
 - `flask db init`
 - `flask db migrate -m "Initial migration."`
 - `flask db upgrade`

# To Run
`python app.py`