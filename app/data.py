from .models import Employment, AchievementResponse, QualificationResponse, SkillResponse, ContactResponse, ContactType
from dotenv import load_dotenv
import os

load_dotenv()

qualification_data = [
    QualificationResponse(
            id=1,
            date="2013 - 2016",
            awarding_body="Sheffield Hallam University",
            qualification="Mathematics BSc (Hons)",
            grade="First Class"
        ),
        QualificationResponse(
            id=2,
            date="2006 - 2013",
            awarding_body="Ashfield Comprehensive School",
            qualification="3 A-Levels",
            grade=None
        ),
        QualificationResponse(
            id=3,
            date="Dec 2020",
            awarding_body="Microsoft",
            qualification="Power BI Data Analyst Associate",
            grade=None
        ),
        QualificationResponse(
            id=4,
            date="Dec 2022",
            awarding_body="Microsoft",
            qualification="Azure Data Engineer Associate",
            grade=None
        ),
        QualificationResponse(
            id=5,
            date="Jan 2022",
            awarding_body="Microsoft",
            qualification="Azure Enterprise Data Analyst Associate",
            grade=None
        ),
        QualificationResponse(
            id=6,
            date="Apr 2024",
            awarding_body="Microsoft",
            qualification="Azure Administrator Associate",
            grade=None
        )
    ]

employment_data = [
    Employment(
            id=1,
            start_date="April 2023",
            end_date=None,
            employer="Harsco Environmental",
            position="Senior Data Engineer",
            achievements=[
                AchievementResponse(id=1, description="Refactored and monitored a generic extract framework within Azure Data Factory for extracting data from 3 ERP systems (Oracle R12, R1229 and JDE) across 30+ countries into our central data warehouse."),
                AchievementResponse(id=2, description="Implemented CI/CD using Azure DevOps to manage build and deployments across 3 separate environments using best practices such as utilising Azure Keyvault, pull requests, branch policies etc."),
                AchievementResponse(id=3, description="Implemented Dbt Core to replace SSIS in order to gain visibility of the data landscape and remove manual configuration of stored procedure executions. Improving overall runtimes and improved CI/CD utilising Docker, Azure Container Registry and Azure Container Instances.")
            ]
        ),
    Employment(
            id=2,
            start_date="June 2021",
            end_date="October 2022",
            employer="Veolia UK",
            position="Data Engineer",
            achievements=[
                AchievementResponse(id=1, description="Created, scheduled and monitored various data pipelines which extracted data and transformed said data from various services (REST & SOAP APIs). Orchestrated via Azure Data Factory (ADF) and managed via CI/CD (Azure Devops)."),
                AchievementResponse(id=2, description="Setup an end to end data pipeline from Workday. Extracted data asynchronously with aiohttp and parsed the xml responses with pyspark. Then staged the data into delta tables within the Lakehouse (ADL gen2), to then be modelled within dbt."),
                AchievementResponse(id=3, description="Authored an in house python package utilising the Google Service API for interacting with Google Sheets and Drive. Published to an Artefact feed (Azure Devops) for versioning and installation purposes."),
                AchievementResponse(id=4, description="Created a Google Sheet Extractor hosted within Azure Functions which was metadata driven and triggered within ADF. Enforcing data quality with the utilisation of python packages such as Great Expectations."),
                AchievementResponse(id=5, description="Created various stored procedures (T-SQL) within Azure Synapse (SQL Data Warehouse).")
            ]
        ),
    Employment(
            id=3,
            start_date="September 2020",
            end_date="June 2021",
            employer="Veolia UK",
            position="Data Analyst",
            achievements=[
                AchievementResponse(id=1, description="Created, scheduled and monitored various data pipelines which extracted data and transformed said data from various services (REST & SOAP APIs). Orchestrated via Azure Data Factory (ADF) and managed via CI/CD (Azure Devops)."),
                AchievementResponse(id=2, description="Setup an end to end data pipeline from Workday. Extracted data asynchronously with aiohttp and parsed the xml responses with pyspark. Then staged the data into delta tables within the Lakehouse (ADL gen2), to then be modelled within dbt."),
                AchievementResponse(id=3, description="Authored an in house python package utilising the Google Service API for interacting with Google Sheets and Drive. Published to an Artefact feed (Azure Devops) for versioning and installation purposes."),
                AchievementResponse(id=4, description="Created a Google Sheet Extractor hosted within Azure Functions which was metadata driven and triggered within ADF. Enforcing data quality with the utilisation of python packages such as Great Expectations."),
                AchievementResponse(id=5, description="Created various stored procedures (T-SQL) within Azure Synapse (SQL Data Warehouse).")
            ]
        ),

    ]

skill_data = [
    SkillResponse(
            id=1,
            description="Python"
        ),
    SkillResponse(
            id=1,
            description="dbt"
        ),
    SkillResponse(
            id=2,
            description="SQL"
        ),
    SkillResponse(
            id=3,
            description="Azure Data Factory"
        ),
    SkillResponse(
            id=4,
            description="Azure Synapse"
        ),
    SkillResponse(
            id=5,
            description="Azure DevOps"
        ),
    SkillResponse(
            id=6,
            description="Azure Functions"
        ),
    SkillResponse(
            id=7,
            description="Azure Data Lake Gen2"
        ),
    SkillResponse(
            id=8,
            description="Databricks"
        ),
    SkillResponse(
            id=9,
            description="Pyspark"
        )
]

contact_data = [
    ContactResponse(
            id=1,
            type=ContactType.EMAIL.value,
            value=os.getenv("EMAIL")
        ),
    ContactResponse(
            id=2,
            type=ContactType.MOBILE.value,
            value=os.getenv("MOBILE")
        ),
    ContactResponse(
            id=3,
            type=ContactType.LINKEDIN.value,
            value=os.getenv("LINKEDIN")
        )
]
