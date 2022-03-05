#settings for the activity
session.set_delimit_liking(enabled=True, max_likes=400, min_likes=10)
session.set_relationship_bounds(enabled=True,
                                max_followers=600,
                                max_following=400,
                                min_followers=50,
                                min_following=20,
                                min_posts=10,
                                max_posts=600)
session.set_user_interact(amount=3, randomize=True, percentage=72, media='Photo')
session.set_do_like(enabled=True, percentage=80)

#activity
session.like_by_tags(['natgeo', 'world'], amount=10, interact=True)



# Interact with the people that a given user is followed by
# set_do_comment, set_do_follow and set_do_like are applicable

session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
session.set_do_like(enabled=False, percentage=70)
session.interact_user_followers(['natgeo'], amount=10, randomize=True)