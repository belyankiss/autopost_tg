class AutopostSettings:
    def __init__(self, name: str,
                 count_post: int,
                 price: float
                 ):
        self.name = name
        self.count_post = count_post
        self.price = price
        PostRouter().include_post(self)

    def __repr__(self):
        return f"name={self.name}, count_post={self.count_post}, price={self.price}"



class PostRouter:
    posts = {}
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    @classmethod
    def include_post(cls, post: AutopostSettings):
        cls.posts[post.name] = (post.count_post, post.price)

    @classmethod
    def include_posts(cls, *posts: AutopostSettings):
        for post in posts:
            cls.posts[post.name] = (post.count_post, post.price)

    def __repr__(self):
        mes = ""
        for post, values in self.posts.items():
            mes += f"name: {post}, count: {values[0]}, price: {values[1]}\n"
        return mes

if __name__ == '__main__':
    new_set = AutopostSettings(name="Open", count_post=3, price=300)
    now_set = AutopostSettings(name="Again", count_post=4, price=450)
    again = AutopostSettings(name="set", count_post=12, price=342)
    router = PostRouter()
    print(router)


