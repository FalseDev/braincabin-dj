from django import template

register = template.Library()


def user_voted_color(votes, user):
    voted = len(votes.filter(pk=user.pk))
    if voted:
        return 'blue'
    return ''


def user_voted_action(votes, user):
    voted = len(votes.filter(pk=user.pk))
    if voted:
        return 'remove'
    return 'add'


def user_upvoted_color(votable_object, user): return user_voted_color(
    votable_object.upvotes, user)


def user_downvoted_color(votable_object, user): return user_voted_color(
    votable_object.downvotes, user)


def user_upvoted_action(votable_object, user): return user_voted_action(
    votable_object.upvotes, user)


def user_downvoted_action(votable_object, user): return user_voted_action(
    votable_object.downvotes, user)


register.filter('user_upvoted_color', user_upvoted_color)
register.filter('user_downvoted_color', user_downvoted_color)
register.filter('user_upvoted_action', user_upvoted_action)
register.filter('user_downvoted_action', user_downvoted_action)
