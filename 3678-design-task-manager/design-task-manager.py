class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.user_tasks = {}
        self.task_map = {}
        self.task_heap = []
        
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)


    def add(self, userId: int, taskId: int, priority: int) -> None:
        if userId not in self.user_tasks:
            self.user_tasks[userId] = {}
        self.user_tasks[userId][taskId] = priority
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.task_heap, (-priority, -taskId))


    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.task_map:
            userId, _ = self.task_map[taskId]
            self.user_tasks[userId][taskId] = newPriority
            self.task_map[taskId] = (userId, newPriority)
            heapq.heappush(self.task_heap, (-newPriority, -taskId))


    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            userId, _ = self.task_map[taskId]
            del self.user_tasks[userId][taskId]
            del self.task_map[taskId]


    def execTop(self) -> int:
        while self.task_heap:
            neg_priority, neg_task_id = heapq.heappop(self.task_heap)
            priority = -neg_priority
            task_id = -neg_task_id
            
            if task_id in self.task_map:
                user_id, current_priority = self.task_map[task_id]
                if current_priority == priority:
                    del self.task_map[task_id]
                    del self.user_tasks[user_id][task_id]
                    return user_id
        return -1
                    


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()