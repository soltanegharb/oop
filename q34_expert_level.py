"""Question: Create a class Plugin with a class attribute registry to keep
track of all plugin instances.
Use a class method to register a new plugin and
a static method to list all registered plugins.
"""










# Iris solution
class Plugin:
    registry = []

    def __init__(self, name):
        self.name = name
        Plugin.registry.append(self)

    @classmethod
    def register_plugin(cls, plugin):
        cls.registry.append(plugin)

    @staticmethod
    def list_plugins():
        return [plugin.name for plugin in Plugin.registry]

# Create instances and register plugins
plugin1 = Plugin("Plugin1")
plugin2 = Plugin("Plugin2")
Plugin.register_plugin(Plugin("Plugin3"))
print(Plugin.list_plugins())  # Output: ['Plugin1', 'Plugin2', 'Plugin3']
