class DB:
    def __init__(self):
        self.user_set = set()
        self.uid_dict = dict()
        self.records = []
    
    def enter(self, uid, nickname):
        self.user_set.add(uid)
        self.uid_dict[uid] = nickname
        self.records.append((uid, '님이 들어왔습니다.'))

    def leave(self, uid):
        self.user_set.remove(uid)
        self.records.append((uid, '님이 나갔습니다.'))

    def change(self, uid, nickname):
        self.uid_dict[uid] = nickname

    def get_message(self):
        return [self.uid_dict[uid] + msg for uid, msg in self.records]

def solution(record):
    database = DB()
    for rec in record:
        ops = rec.split()
        if ops[0] == 'Enter':
            database.enter(ops[1], ops[2])
        elif ops[0] == 'Leave':
            database.leave(ops[1])
        elif ops[0] == 'Change':
            database.change(ops[1], ops[2])
    
    return database.get_message()

record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
    ]

result = [
    "Prodo님이 들어왔습니다.", 
    "Ryan님이 들어왔습니다.", 
    "Prodo님이 나갔습니다.", 
    "Prodo님이 들어왔습니다."
]

print(solution(record) == result)

# 1234 무지 들어옴
# 4567 프로도 들어옴
# 1234 나감
# 1234 프로도 닉바꾸고 들어옴
# 4567 라이언으로 바꿈

# 1234 프로도 들어옴
# 4567 라이언 들어옴
# 1234 프로도 나감
# 1234 프로도 들어옴