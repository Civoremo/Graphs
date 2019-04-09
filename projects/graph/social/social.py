import random

class Queue:
    def __init__(self):
        self.queue_size = 0
        self.storage = []

    def enqueue(self, item):
        self.queue_size += 1
        self.storage.append(item)

    def dequeue(self):
        if self.queue_size > 0:
            self.queue_size -= 1
            return self.storage.pop(0)

    def size(self):
        return self.queue_size

    def isEmpty(self):
        return self.storage == []



class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(0, numUsers):
            self.addUser(f'User {user}')

        # Create friendships
        possibleFriendships = []

        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append([userID, friendID])
                # print(f'{possibleFriendships}')

        random.shuffle(possibleFriendships)

        for i in range(numUsers * avgFriendships // 2):
            friendship = possibleFriendships[i]
            # print(f'I: {i} friendship: {friendship}')
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = Queue()
        queue.enqueue([userID])
        
        # userFriends = self.friendships[userID].copy()
        # print(f'Values: {userFriends}')
        # for friend in userFriends:
        #     print(f'friend: {friend}')

        while queue.size() > 0:
            path = queue.dequeue()
            user = path[-1]
            if user not in visited:
                # print(f"Current User: {user}, Current Path: {path}")
                visited[user] = path
                for neighbor in self.friendships[user]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)
        visited = {key: value for key,
                   value in visited.items() if value != set()}

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
