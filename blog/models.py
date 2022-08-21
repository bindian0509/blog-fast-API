import datetime


from redis_om import get_redis_connection, EmbeddedJsonModel, JsonModel, Field, Migrator

#REDACTED 
redis = get_redis_connection(
    host="#############",
    port=0,
    password="#################",
    decode_responses=True,
)

class Author(EmbeddedJsonModel):
    first_name: str = Field(index=True, full_text_search=True)
    last_name: str
    email: str
    bio: str
    date_joined: datetime.date = Field(default=datetime.datetime.now())

    class Meta:
        database = redis


class Blog(JsonModel):
    title: str = Field(index=True, full_text_search=True)
    content: str
    author: Author
    date_posted: datetime.date = Field(
        default=datetime.datetime.today().strftime("%Y-%m-%d")
    )

    class Meta:
        database = redis


Migrator().run()


