import yaml #version 5.2

class Foo:
    def _init_(self):
        self.bar = 42

print(yaml.dump(Foo()))
print(yaml.dump(yaml.full_load(yaml.dump(Foo()))))

print(yaml.dump((1,2,3)))
print(yaml.dump(yaml.load(yaml.dump((1,2,3)))))
