from flask import Flask
import firebase_admin
from firebase_admin import credentials, auth, messaging

app = Flask(__name__)

import RegistrationController
import TrackerController
import MCServerStatusController
import PersonalController
import PowerManagementController
import ServiceStatusController