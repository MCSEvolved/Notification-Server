from __main__ import app
from flask import Flask, jsonify, request
from NotificationService import *

@app.route('/api/service-status/tracker', methods=['POST'])
def trackerDownNotification():
    topic:str = "topic/service-status/tracker"

    return "", 201

@app.route('/api/service-status/storage', methods=['POST'])
def storageDownNotification():
    topic:str = "topic/service-status/storage"
    return "", 201

@app.route('/api/service-status/emerald-exchange', methods=['POST'])
def emeraldExchangeDownNotification():
    topic:str = "topic/service-status/emerald-exchange"
    return "", 201


@app.route('/api/service-status/reactor-manager', methods=['POST'])
def reactorManagerDownNotification():
    topic:str = "topic/service-status/reactor-manager"
    return "", 201
