"""
    CHANGELOGEN 
    Simple Changelog Generator for Github Log
    Copyright (C) 2021 Bengart Zakhar

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Description:
        Main module for CHANGELOGEN

    Author:
        Bengart Zakhar
"""

import os
import subprocess

class Changelogen():
    def __init__(self, log_format='md'):
        self.logs = []
        self.tags = []
        self.log_format = log_format
        self.data = []

    def get_tag(self):
        tags = subprocess.check_output('git tag --sort=-creatordate', shell=True)
        self.tags = tags.decode("utf-8").splitlines()

    def get_commit(self):
        #if len(self.tags) < 1:
        #    return
        prev_tag = ""
        #self.tags[0]
        for tag in self.tags:
            cmd = "git log -1 --pretty=format:'%ad' --date=short " + tag
            tag_date = subprocess.check_output(cmd, shell=True).decode("utf-8")
            self.data.append('\n## `' + prev_tag + '` ' + tag_date)
            cmd = "git log " + tag + "..." + prev_tag + " --pretty=format:'%s'"
            commits_raw = subprocess.check_output(cmd, shell=True)
            commits_raw = commits_raw.decode("utf-8").splitlines()
            commits = {}
            other_commit = []
            for commit in commits_raw:
                if 'Merge' in commit:
                    continue
                commit_split = commit.split(':')
                if len(commit_split) > 1:
                    if commit_split[0] in commits:
                        if commit_split[1] not in commits[commit_split[0]]:
                            commits[commit_split[0]].append(commit_split[1])
                    else:
                        commits[commit_split[0]] = [commit_split[1],]
                else:
                    if commit_split[0] not in other_commit:
                        other_commit.append(commit_split[0])
            if other_commit:
                commits['other'] = other_commit
            for commit in commits:
                self.data.append('\n_' + commit + '_  ')
                for c in commits[commit]:
                    self.data.append('- ' + c.strip() + '  ')
            prev_tag = tag

    def save(self):
        with open("CHANGELOG.md", "w") as f:
            f.write("\n".join(self.data))

    def print(self):
        for d in self.data:
            print(d)

def main(log_format='md'):
    changelogen = Changelogen(log_format)
    changelogen.get_tag()
    changelogen.get_commit()
    changelogen.print()
    changelogen.save()