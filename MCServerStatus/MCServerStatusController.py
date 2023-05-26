from __main__ import app
from flask import Flask, jsonify, request

@app.route('/api/mc-server/shut-off', methods=['POST'])
def mcServerShutOffNotification():
    topic:str = "topic/mc-server"
    return "", 201

@app.route('/api/mc-server/shut-on', methods=['POST'])
def mcServerShutOnNotification():
    topic:str = "topic/mc-server"
    return "", 201