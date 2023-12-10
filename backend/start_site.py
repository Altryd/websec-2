from app import app
from app.routes.api import api_routes
"""
from app.api.reservation import reservation_api
from app.api.warcomm import warcomm_api
from app.api.VYS import vys_api
from app.api.training_group import training_group_api
from app.api.utility import utility_api
from app.api.platoon import platoon_api
from app.api.professors import professors_api
from app.api.login import login_api
from app.api.entry import entry_api
from app.api.personal_data import personal_data_api
from app.api.student import student_api
from app.api.statistics import statistics_api
from app.api.suspension_order import suspension_api

from app.api.military_training import military_training_api

from app.routes_folder.personnel import personnel_routes
from app.routes_folder.professor import professor
from app.routes_folder.admin import admin_routes
from app.routes_folder.docx_export import docx_export_routes
from app.routes_folder.edit_personnel import edit_personnel_routes
from app.routes_folder.entry import entry
from app.routes_folder.entry_documents import entry_documents_routes
from app.routes_folder.excel_export import excel_export
from app.routes_folder.instruments import instrument_routes
from app.routes_folder.login import login_routes
from app.routes_folder.news import news_routes
from app.routes_folder.training_military import training_military_routes
"""


if __name__ == "__main__":
    app.register_blueprint(api_routes)
    """
    app.register_blueprint(warcomm_api)
    app.register_blueprint(vys_api)
    app.register_blueprint(training_group_api)
    app.register_blueprint(utility_api)
    app.register_blueprint(platoon_api)
    app.register_blueprint(professors_api)
    app.register_blueprint(login_api)
    app.register_blueprint(entry_api)
    app.register_blueprint(personal_data_api)
    app.register_blueprint(student_api)
    app.register_blueprint(statistics_api)
    app.register_blueprint(suspension_api)
    app.register_blueprint(reservation_api)
    app.register_blueprint(military_training_api)

    app.register_blueprint(personnel_routes)
    app.register_blueprint(professor)
    app.register_blueprint(admin_routes)
    app.register_blueprint(docx_export_routes)
    app.register_blueprint(edit_personnel_routes)
    app.register_blueprint(entry)
    app.register_blueprint(entry_documents_routes)
    app.register_blueprint(excel_export)
    app.register_blueprint(instrument_routes)
    app.register_blueprint(login_routes)
    app.register_blueprint(news_routes)
    app.register_blueprint(training_military_routes)
    """

    app.run(debug=True)
