import requests
import argparse

event_types = ['PushEvent', 'PullRequestEvent', 'IssuesEvent', 'IssueCommentEvent',
               'CreateEvent', 'DeleteEvent', 'ForkEvent', 'WatchEvent', 'ReleaseEvent',
               'PublicEvent', 'PullRequestReviewCommentEvent']


def parse_arguments():
    parser = argparse.ArgumentParser(description="GitHub Events Viewer CLI")

    subparsers = parser.add_subparsers(dest="command", required=True)

    event_parser = subparsers.add_parser(
        "events", help="Display recent GitHub events")
    event_parser.add_argument("username", type=str, help="GitHub username")
    event_parser.add_argument("--sort", type=str, default='',
                              help="Filter event type ('PushEvent', 'PullRequestEvent', 'IssuesEvent', 'IssueCommentEvent','CreateEvent', 'DeleteEvent', 'ForkEvent', 'WatchEvent', 'ReleaseEvent','PublicEvent', 'PullRequestReviewCommentEvent')")

    return parser.parse_args()


def fetch_events(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"failed to fetch events:{response.status_code}")


def count_events(events):
    event_types = ['PushEvent', 'PullRequestEvent', 'IssuesEvent', 'IssueCommentEvent',
                   'CreateEvent', 'DeleteEvent', 'ForkEvent', 'WatchEvent', 'ReleaseEvent',
                   'PublicEvent', 'PullRequestReviewCommentEvent']
    events_count = []
    for event_type in event_types:
        counter = 0
        for event in events:
            if event['type'] == event_type:
                counter += 1
        events_count.append(counter)
    print(f"{'Event Type':<15}{'Count':<2}")
    print("-"*25)
    for i, event_type in enumerate(event_types):
        if events_count[i] != 0:
            print(f"{event_type:<15}{events_count[i]}")
        # def PushEvent():
    print("-"*25)


def show_events(events, sort=''):
    if sort != '' and sort not in event_types:
        print("sorting arugment not available please use: ('PushEvent', 'PullRequestEvent', 'IssuesEvent', 'IssueCommentEvent','CreateEvent', 'DeleteEvent', 'ForkEvent', 'WatchEvent', 'ReleaseEvent','PublicEvent', 'PullRequestReviewCommentEvent')")
    for event in events:
        event_type = event['type']
        if sort and event_type != sort:
            continue

        actor = event.get('actor', {}).get('login', 'Unknown User')
        repo = event.get('repo', {}).get('name', 'Unknown Repo')
        if event_type == 'PushEvent':
            print(f"{actor} pushed to {event['repo']['name']}.")
        elif event_type == 'PullRequestEvent':
            print(
                f"{actor} {event['payload']['action']} a pull request {event['payload']['pull_request']['number']}.")
        elif event_type == 'IssuesEvent':
            print(
                f"{actor} {event['payload']['action']} an issue event {event['payload']['issue']['number']}.")
        elif event_type == 'IssueCommentEvent':
            print(
                f"{actor} {event['payload']['action']} an issue comment {event['payload']['issue']['number']}.")
        elif event_type == 'CreateEvent':
            print(
                f"{actor} created {event['payload']['ref_type']} {event['payload']['ref']}.")
        elif event_type == 'DeleteEvent':
            print(
                f"{actor} Deleted {event['payload']['ref_type']} {event['payload']['ref']}.")
        elif event_type == 'ForkEvent':
            print(
                f"{actor} forked {event['payload']['forkee']}.")
        elif event_type == 'WatchEvent':
            print(
                f"{actor} {event['payload']['action']} watched {repo}.")
        elif event_type == 'ReleaseEvent':
            print(
                f"{actor} {event['payload']['action']} released {event['payload']['release']}.")
        elif event_type == 'PublicEvent':
            print(
                f"{actor} made public  {repo}.")
        elif event_type == 'PullRequestReviewCommentEvent':
            print(
                f"{actor} {event['payload']['action']} commented on a pull request {event['payload']['pull_request']['number']}.")
        else:
            print(f"{actor}:{event_type}")


def main():
    args = parse_arguments()
    events = fetch_events(args.username)

    if args.command == "events":
        count_events(events)
        show_events(events, args.sort)


if __name__ == "__main__":
    main()
