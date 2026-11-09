class Project:
    def __init__(self, name, description, dependencies, development_dependencies, license="", authors=None):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.development_dependencies = development_dependencies
        self.license = license
        self.authors = authors if authors is not None else []

    def __str__(self):
        result = f"Name: {self.name}\n"
        result += f"Description: {self.description}\n"
        
        if self.license:
            result += f"License: {self.license}\n"
            
        if self.authors:
            result += "\nAuthors:\n"
            for author in self.authors:
                result += f"- {author}\n"
                
        result += "\nDependencies:\n"
        if self.dependencies:
            for dep in self.dependencies:
                result += f"- {dep}\n"
        else:
            result += "-\n"
            
        result += "\nDevelopment dependencies:\n"
        if self.development_dependencies:
            for dev_dep in self.development_dependencies:
                result += f"- {dev_dep}\n"
        else:
            result += "-\n"
            
        return result.strip()