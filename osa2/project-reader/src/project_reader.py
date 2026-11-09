from urllib import request
import tomllib
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomllib.loads(content)

        # Haetaan [project]-osio
        project_data = data.get("project", {})
        
        name = project_data.get("name", "")
        description = project_data.get("description", "")
        
        # Haetaan lisenssi (voi olla merkkijono tai sanakirja, esim. {"text": "MIT"} tai "MIT")
        license_raw = project_data.get("license", "")
        if isinstance(license_raw, dict):
            license_name = license_raw.get("text", "")
        else:
            license_name = str(license_raw)

        # Haetaan tekijät (authors on yleensä lista sanakirjoja, joissa on "name")
        authors_raw = project_data.get("authors", [])
        authors = []
        for author in authors_raw:
            if isinstance(author, dict) and "name" in author:
                authors.append(author["name"])
            elif isinstance(author, str):
                authors.append(author)

        # Puhdistetaan riippuvuuksien nimet (poistetaan >=, ==, < jne.)
        raw_dependencies = project_data.get("dependencies", [])
        dependencies = []
        for dep in raw_dependencies:
            clean_dep = dep
            for op in [">=", "<=", "==", "~=", "!=", ">", "<", "@", ";"]:
                clean_dep = clean_dep.split(op)[0]
            dependencies.append(clean_dep.strip())

        # Kehitysaikaiset riippuvuudet (uusi dependency-groups tai vanha dev-dependencies)
        raw_dev_dependencies = data.get("dependency-groups", {}).get("dev", [])
        if not raw_dev_dependencies:
            raw_dev_dependencies = data.get("dev-dependencies", [])

        dev_dependencies = []
        for dep in raw_dev_dependencies:
            clean_dep = dep
            for op in [">=", "<=", "==", "~=", "!=", ">", "<", "@", ";"]:
                clean_dep = clean_dep.split(op)[0]
            dev_dependencies.append(clean_dep.strip())

        return Project(name, description, dependencies, dev_dependencies, license_name, authors)