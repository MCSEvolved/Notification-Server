from __main__ import app
from flask import Flask, jsonify, request

@app.route('/api/power-management/shortage', methods=['POST'])
def powerShortageNotification():
    topic:str = "topic/power-management/shortage"
    return "", 201

@app.route('/api/power-management/reactor-shut-off', methods=['POST'])
def ReactorShutOffNotification():
    topic:str = "topic/power-management/reactor-shut-off"
    return "", 201