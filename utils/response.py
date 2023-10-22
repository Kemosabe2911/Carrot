class EventSchedulerResponse:
    def __init__(self, name, desc, type, completed_at, is_completed):
        self.name = name
        self.desc = desc
        self.type = type
        self.completed_at = completed_at
        self.is_completed = is_completed

# Custom serialization function for EventSchedulerResponse
def SerializeEventScheduler(obj):
    if isinstance(obj, EventSchedulerResponse):
        return {
            'name': obj.name, 
            'desc': obj.desc, 
            'type': obj.type,
            'completed_at': obj.completed_at.isoformat(),
            'is_completed': obj.is_completed 
        }
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
