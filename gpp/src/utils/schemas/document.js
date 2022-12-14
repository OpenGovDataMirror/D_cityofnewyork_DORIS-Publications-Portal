export default {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "properties": {
    "creators": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "date_published": {
      "pattern": "\\d{2}/\\d{2}/\\d{4}",
      "type": "string",
      "error": {
        "pattern": "This is not a valid date value."
      }
    },
    "description": {
      "maxLength": 200,
      "minLength": 100,
      "type": "string",
      "error": {
        "maxLength": "Please shorten your description to at most 200 characters.",
        "minLength": "Please lengthen your description to at least 100 characters."
      }
    },
    "end_date": {
      "pattern": "\\d{2}/\\d{2}/\\d{4}",
      "type": "string",
      "error": {
        "pattern": "This is not a valid date value."
      }
    },
    "files": {
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "title": {
            "type": "string",
            "maxLength": 140,
            "minLength": 3
          }
        },
        "required": [
          "name",
          "title"
        ]
      },
      "type": "array",
      "minItems": 1
    },
    "report_type": {
      "type": "string",
      "enum": [
        "adjudications_decisions",
        "audit_report",
        "brochures",
        "budget_finance",
        "bulletins",
        "calendars",
        "data_statistics",
        "directives",
        "environmental_impact_statements_draft",
        "environmental_impact_statements_final",
        "executive_orders",
        "guides",
        "laws_legislation",
        "manuals_directories",
        "minutes",
        "newletters",
        "other",
        "plans",
        "press_releases",
        "proceedings",
        "reports_annual",
        "reports_biennial",
        "reports_monthly",
        "reports_weekly",
        "reports_other",
        "studies"
      ],
      "error": {
        "enum": "This is not a valid report type.",
        "required": "You must choose a report type."
      }
    },
    "start_date": {
      "pattern": "\\d{2}/\\d{2}/\\d{4}",
      "type": "string",
      "error": {
        "pattern": "This is not a valid date value."
      }
    },
    "subjects": {
      "items": {
        "type": "string",
        "enum": [
          "accounting",
          "advertising",
          "aged",
          "alcohol",
          "animal_welfare",
          "archaeology",
          "architecture",
          "art_design",
          "athletics",
          "banks_banking",
          "borough_brooklyn",
          "borough_bronx",
          "city_brooklyn",
          "budget_finance",
          "building_code",
          "building_construction",
          "buildings",
          "business",
          "celebrations_parades",
          "cemeteries",
          "census",
          "charities",
          "children",
          "city_planning",
          "civil_service",
          "climate",
          "coastal",
          "community_relations",
          "consumers",
          "conventions",
          "correction",
          "cost",
          "courts",
          "crime_criminals",
          "criminal_justice",
          "culture",
          "data_communications",
          "death",
          "demography_population",
          "disability",
          "discrimination",
          "disease",
          "drugs",
          "education",
          "education_bilingual",
          "education_prekinder",
          "education_remedial",
          "education_special",
          "elections_voting",
          "electric_power",
          "emergencies",
          "employment",
          "energy",
          "engineering",
          "environment",
          "equal_employment",
          "ethics",
          "ethnic_groups",
          "families",
          "finance",
          "fire_fighting",
          "firearms",
          "food",
          "food_supply",
          "fuels",
          "gambling",
          "geography",
          "government",
          "government_citizen_participation",
          "hazardous_materials",
          "health",
          "history",
          "homeless_persons",
          "hospitals",
          "hotels",
          "housing",
          "housing_limited_profit",
          "housing_low_income",
          "human_rights",
          "immigration",
          "industries",
          "infrastructure",
          "insurance",
          "internet",
          "islands",
          "labor_employment",
          "land_use",
          "landmarks",
          "languages",
          "laws_legislation",
          "lgbtq",
          "libraries",
          "licenses_permits",
          "borough_manhattan",
          "maps",
          "markets",
          "mayor_name",
          "memorials",
          "mental_health",
          "monuments",
          "motor_vehicles",
          "museums",
          "neighborhoods",
          "nutrition",
          "officials_employees",
          "parking",
          "parks_recreation",
          "pensions",
          "pests",
          "police",
          "police_community_relations",
          "police_discipline",
          "politics_government",
          "pollution",
          "poverty",
          "prices",
          "purchasing_methods",
          "public_authorities",
          "public_welfare",
          "borough_queens",
          "real_property",
          "records",
          "recreation",
          "recycling",
          "refuse_disposal",
          "religions",
          "rent_control",
          "rent_stabilization_law",
          "restaurants",
          "retail",
          "rivers",
          "sanitation",
          "schools",
          "schools_administration",
          "schools_charter",
          "schools_parochial",
          "schools_private",
          "schools_buildings",
          "sewage",
          "small_business",
          "snow_removal",
          "special_districts",
          "state_new_york",
          "borough_staten_island",
          "statistics",
          "statistics_education",
          "statistics_police",
          "street_vendors",
          "streets_maintenance_repair",
          "streets_highways",
          "students",
          "subways",
          "subways_stations",
          "supplies",
          "surveying",
          "taxation",
          "taxation_exemption",
          "taxation_real_property",
          "taxicabs",
          "teachers",
          "television",
          "terminals",
          "terrorism",
          "toilets",
          "toils",
          "tourists",
          "traffic_parking",
          "traffic_safety",
          "transit",
          "transit_rapid",
          "transportation",
          "transportation_finance",
          "transportation_school",
          "transportation_planning",
          "trees",
          "trusts_estates",
          "universities_colleges",
          "vendors_contracts",
          "veterans",
          "volunteers",
          "water",
          "water_supply",
          "weapons",
          "weather",
          "women",
          "world_trade_center",
          "youth"
        ]
      },
      "minItems": 1,
      "maxItems": 3,
      "type": "array",
      "error": {
        "maxItems": "You can only choose up to 3 subjects.",
        "minItems": "You must choose at least 1 subject."
      }
    },
    "subtitle": {
      "maxLength": 150,
      "type": "string",
      "error": {
        "maxLength": "Please shorten your subtitle to at most 150 characters."
      }
    },
    "title": {
      "maxLength": 150,
      "minLength": 10,
      "type": "string",
      "error": {
        "maxLength": "Please shorten your title to at most 150 characters.",
        "minLength": "Please lengthen your title to at least 10 characters."
      }
    },
    "agency": {
      "type": "string",
      "error": {
        "required": "You must choose an agency."
      }
    },
    "year": {
      "minimum": 1600,
      "type": "integer",
      "error": {
        "minimum": "This year cannot be earlier than 1600.",
        "type": "This field is required and cannot be earlier than 1600."
      }
    },
    "year_type": {
      "type": "string"
    },
    "language": {
      "type": "string",
      "enum": [
        "english",
        "spanish",
        "chinese",
        "russian",
        "arabic",
        "bengali",
        "french",
        "haitian_creole",
        "italian",
        "korean",
        "polish",
        "urdu",
        "yiddish"
      ],
      "error": {
        "enum": "This is not a valid language.",
        "required": "You must choose a language."
      }
    }
  },
  "required": [
    "files",
    "agency",
    "description",
    "title",
    "date_published",
    "subjects",
    "language",
    "report_type",
    "year_type"
  ],
  "anyOf": [
    {
      "required": [
        "year"
      ]
    },
    {
      "required": [
        "end_date",
        "start_date"
      ]
    }
  ],
  "type": "object",
};