class ConversationBufferMemory:
    def __init__(self):
        self.histories = {}

    def get_history(self, session_id):
        if session_id not in self.histories:
            self.histories[session_id] = []
        return self.histories[session_id]

    def add_message(self, session_id, role, content):
        if session_id not in self.histories:
            self.histories[session_id] = []
        self.histories[session_id].append({"role": role, "content": content})

    def clear_history(self, session_id):
        if session_id in self.histories:
            self.histories[session_id] = []
# Simulated change on 2023-01-05 17:55:00
# Simulated change on 2023-01-05 11:01:00
# Simulated change on 2023-02-01 11:10:00
# Simulated change on 2023-02-22 14:30:00
# Simulated change on 2023-03-09 10:52:00
# Simulated change on 2023-03-14 09:28:00
# Simulated change on 2023-04-11 15:06:00
# Simulated change on 2023-04-13 17:08:00
# Simulated change on 2023-04-24 17:04:00
# Simulated change on 2023-05-10 09:08:00
# Simulated change on 2023-05-10 13:10:00
# Simulated change on 2023-06-05 09:48:00
# Simulated change on 2023-06-06 15:18:00
# Simulated change on 2023-06-12 12:36:00
# Simulated change on 2023-06-13 18:01:00
# Simulated change on 2023-06-30 12:52:00
# Simulated change on 2023-07-03 12:04:00
# Simulated change on 2023-07-05 16:27:00
# Simulated change on 2023-07-14 18:52:00
# Simulated change on 2023-07-19 13:39:00
