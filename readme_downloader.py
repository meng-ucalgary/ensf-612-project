# File:         readme_downloader.py
# Author:       Bhavyai Gupta
# Description:  Randomly downloads unique README files from GitHub

import json
import logging
import numpy as np
import os
import pandas as pd
import random
import requests


class Readme:
    logging.basicConfig(level=logging.INFO, filename='readme_downloader.log', filemode='w',
                        format='%(asctime)s [%(levelname)s] Line: %(lineno)d, Message: %(message)s')

    def __init__(self):
        '''
        Attributes:
            _readme_count (int)
            _request_countdown (int)

            _api_repository_url (str)
            _api_repo_base_url (str)
            _api_raw_url (str)
            _api_header (dict)

            _directory_research_data (str)
            _original_repos_nd (ndarray)

            _directory_project_data (str)
            _project_data_path (str)
            _new_repos_df (dataframe)

            _default_folders (list)
            _markdown_name (list)
            _markdown_exts (list)
        '''

        # variables to track how many README files we want to download and how many we can
        # --------------------------------------------------------------------------------
        self._readme_count = 20
        self._request_countdown = 1
        # --------------------------------------------------------------------------------

        # create the api urls
        # --------------------------------------------------------------------------------
        self._api_repository_url = 'https://api.github.com/repositories'
        self._api_repo_base_url = 'https://api.github.com/repos'
        self._api_raw_url = 'https://raw.githubusercontent.com'
        # --------------------------------------------------------------------------------


        # create the api_header
        # --------------------------------------------------------------------------------
        git_pat_path = r'D:\\GitHub\\PAT.txt'

        if os.path.exists(git_pat_path):
            logging.info(f'GitHub PAT accessed at {git_pat_path}')
            f = open(git_pat_path, mode='r', encoding='utf-8')
            token = f.readline().strip()
            self._api_header = {'accept': 'application/vnd.github.v3+json', 'authorization': 'token ' + token}
            f.close()

        else:
            self._api_header = {'accept': 'application/vnd.github.v3+json'}
        # --------------------------------------------------------------------------------


        # seed the random for 'since' in get_api_options()
        # --------------------------------------------------------------------------------
        random.seed(10)
        # --------------------------------------------------------------------------------


        # read the file for existing dataset used in research paper
        # --------------------------------------------------------------------------------
        self._directory_research_data = 'research_data'
        research_data_filename = 'dataset_combined.csv'
        original_repos_df = pd.read_csv(os.path.join(self._directory_research_data, research_data_filename), usecols=["url"])
        self._original_repos_nd = original_repos_df.drop_duplicates().reset_index(drop=True).values
        # --------------------------------------------------------------------------------


        # read or create file to track new dataset
        # --------------------------------------------------------------------------------
        self._directory_project_data = 'project_data'
        project_data_filename = 'new_dataset.csv'
        self._project_data_path = os.path.join(self._directory_project_data, project_data_filename)

        if not os.path.exists(self._directory_project_data):
            os.makedirs(self._directory_project_data)

        if os.path.exists(self._project_data_path):
            logging.info(f'Project dataset file already exists {self._project_data_path}')
            self._new_repos_df = pd.read_csv(self._project_data_path, usecols=['url', 'readme_location', 'saved_as'])

        else:
            logging.info(f'Creating project dataset file {self._project_data_path}')
            self._new_repos_df = pd.DataFrame(columns=['url', 'readme_location', 'saved_as'])
            self._new_repos_df.to_csv(self._project_data_path, header=True)
        # --------------------------------------------------------------------------------


        # create lists to track supported folder, name, and extensions of README files
        # --------------------------------------------------------------------------------
        # https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
        self._default_folders = [None, '.github', 'docs']

        # we check both uppercase and lowercase
        self._markdown_name = ['README', 'readme']

        # https://github.com/github/markup/blob/master/README.md
        # markdown_exts_small = ['.adoc', '.asciidoc', '.creole', '.markdown', '.md', '.mdown', '.mediawiki', '.mkdn', '.org', '.pod', '.rdoc', '.rst', '.textile', '.wiki', '.asc']
        markdown_exts_small = ['.md', '.markdown', '.mdown', '.mkdn', '.adoc', '.asciidoc', '.creole', '.mediawiki',
                                '.org', '.pod', '.rdoc', '.rst', '.textile', '.wiki', '.asc']

        self._markdown_exts = []

        for m in markdown_exts_small:
            self._markdown_exts.append(m)
            self._markdown_exts.append(m.upper())
        # --------------------------------------------------------------------------------


    def get_api_options(self):
        '''
        Returns updated api_options with a random number within the limit
        according to the research paper
        '''

        api_options = {'since': random.randrange(0, 100000000, 1)}
        return api_options


    def fetch_request(self, api_url, api_headers=None, api_options=None):
        '''
        Fetches the response of the request of api_url using options
        api_headers and api_options
        '''

        logging.info(f'Fetching request at {api_url}')
        r = requests.get(api_url, headers=api_headers, params=api_options)
        return r


    def fetch_json(self, api_url, api_headers=None, api_options=None):
        '''
        Fetches the JSON response using the api_url, api_headers,
        and api_options
        '''

        r = self.fetch_request(api_url, api_headers, api_options)

        if r.status_code != requests.codes.ok:
            return (r.status_code, None, None)

        return (r.status_code, dict(r.headers), json.loads(r.text))


    def check_existing(self, repo_url):
        '''
        Checks if repo_url exists in the ndarray original_repos_nd
        '''

        if repo_url in self._original_repos_nd:
            logging.info(f'Found {repo_url} in research dataset')
            return True

        return False


    def check_new(self, repo_url):
        '''
        Checks if repo_url exists in the ndarray new_repos_nd
        '''

        # extract the column 'url' from the dataset new_repos_df
        new_repos_nd = self._new_repos_df['url'].values

        if repo_url in new_repos_nd:
            logging.info(f'Already accessed repo at {repo_url}')
            return True

        return False


    def save_file(self, qualified_name, html_url, request):
        '''
        Saves the contents of the request as name derived from
        qualified_name in the directory directory_project_data
        '''

        if qualified_name[2] is None:
            filename = ".".join(qualified_name[0].split('/') + [qualified_name[1], qualified_name[3]])
            readme_location = str(qualified_name[3])

        else:
            filename = ".".join(qualified_name[0].split('/') + qualified_name[1:])
            readme_location = str(qualified_name[2] + '/' + qualified_name[3])

        with open(os.path.join(self._directory_project_data, filename), 'wb') as fd:
            logging.info(f'Saving readme as {filename}')
            for chunk in request.iter_content(chunk_size=128):
                fd.write(chunk)


        self._new_repos_df = self._new_repos_df.append({'url': html_url, 'readme_location': readme_location, 'saved_as': filename},
                                                        ignore_index=True)
        self._new_repos_df.to_csv(self._project_data_path, header=True)


    def find_readme(self, repo_name, default_branch):
        '''
        Finds and returns the downloadable url of a readme of
        repo repo_name, if the README exists
        '''

        repo_raw_url = self._api_raw_url + '/' + repo_name

        for x in self._default_folders:
            for y in self._markdown_name:
                for z in self._markdown_exts:
                    test_url = ''

                    if x is None:
                        test_url = repo_raw_url + '/' + default_branch + '/' + y + z

                    else:
                        test_url = repo_raw_url + '/' + default_branch + '/' + x + '/' + y + z

                    logging.info(f'Finding README at {test_url}')

                    if self.fetch_request(test_url).status_code == requests.codes.ok:
                        return test_url, [repo_name, default_branch, x, y+z]

        return None, None


    def download(self):
        '''
        Downloads randon README files
        '''

        while(self._request_countdown > 0 and self._readme_count != 0):
            # fetch the list of repositories
            response_code, repository_header, repository_array = self.fetch_json(
                self._api_repository_url, api_headers=self._api_header, api_options=self.get_api_options())

            if response_code != requests.codes.ok:
                continue

            # update the value of remaining API calls
            self._request_countdown = int(repository_header['X-RateLimit-Remaining'])
            logging.info(f'Remaining API calls {self._request_countdown}')

            # loop through all items in the repository_array
            while(self._request_countdown > 0 and self._readme_count != 0 and len(repository_array) != 0):
                # fetch one item from the JSON array
                repository = repository_array.pop()

                # if repo was in original dataset, skip it
                if self.check_existing(repository['html_url']):
                    continue

                # if repo is already downloaded, skip it
                elif self.check_new(repository['html_url']):
                    continue

                else:
                    # create the API url for the repo details
                    api_repo_url = self._api_repo_base_url + "/" + repository['full_name']

                    # fetch details for the repo
                    response_code, repo_header, repo_response = self.fetch_json(
                        api_repo_url, api_headers=self._api_header)

                    if response_code != requests.codes.ok:
                        continue

                    # update the value of remaining API calls
                    self._request_countdown = int(repo_header['X-RateLimit-Remaining'])
                    logging.info(f'Remaining API calls {self._request_countdown}')

                    # if the repo is not a Software Development repo, skip it
                    if repo_response['language'] is None:
                        logging.info(f'Ignoring non SD readme at {repo_response["html_url"]}')
                        continue

                    else:
                        readme_url, qualified_name = self.find_readme(
                            repo_response['full_name'], repo_response['default_branch'])

                        # if the repo doesn't has any readme, skip it
                        if readme_url is None:
                            continue

                        else:
                            sr = self.fetch_request(readme_url, api_headers=self._api_header)

                            # if the README size is less than 2KB, ignore the file
                            if sr.content.__len__() < 2048:
                                logging.info(f'Ignoring small readme at {readme_url}')
                                continue

                            self.save_file(qualified_name, repo_response['html_url'], sr)
                            self._readme_count -= 1
                            logging.info(f'Remaining files to download {self._readme_count}')


if __name__ == '__main__':
    x = Readme()
    x.download()
