topics = [
    "mc-server",
    "user_weekly-report",
    "power-management_shortage",
    "power-management_reactor-shut-off",
    "service-status_tracker",
    "service-status_storage",
    "service-status_emerald-exchange",
    "service-status_reactor-manager",
    "tracker_error",
    "tracker_warning",
    "tracker_out-of-fuel"
]

def topicExists(topic:str):
    if topic in topics:
        return True
    else:
        return False