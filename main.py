import requests
import json
from input import *


def get_competition_id(name, country):
    response = requests.get('https://api.football-data.org/v2/competitions/', headers=HEADER)
    parsed_response = json.loads(response.text)
    for competition in parsed_response['competitions']:
        if competition['area']['name'] == country and competition['name'] == name:
            return competition['code'], competition['id']


def get_team_id(competition_id, team):
    response = requests.get('https://api.football-data.org/v2/competitions/' + str(competition_id) + '/teams', headers=HEADER)
    parsed_response = json.loads(response.text)
    for team_json in parsed_response['teams']:
        if team_json['name'] == team:
            return team_json['id']


def get_team_matches(team_id):
    scheduled_matches_response = requests.get('https://api.football-data.org/v2/teams/' + str(team_id)
                                              + '/matches?status=SCHEDULED', headers=HEADER)
    parsed_scheduled_matches = json.loads(scheduled_matches_response.text)
    return parsed_scheduled_matches


def print_team_matches(team_matches):
    print(TEAM + ' next matches are: ')
    for match in team_matches['matches']:
        print(' *  ' + match['homeTeam']['name'] + ' vs ' + match['awayTeam']['name'] + ' (' + match['utcDate'] + ')')


def main():
    competition_code, competition_id = get_competition_id(COMPETITION_NAME, COUNTRY)
    team_id = get_team_id(competition_id, TEAM)
    team_matches = get_team_matches(team_id)
    print_team_matches(team_matches)


if __name__ == "__main__":
    main()