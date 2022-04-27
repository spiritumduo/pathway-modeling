import yaml


with open("pathway_model.yaml", "r") as file:
    test_data = yaml.safe_load(file)

def try_loading():
    print(test_data)

class TestKeywordPathway:
    '''Test that we have the pathway keyword and it is of type str'''
    key = "pathway"
            
    def test_keyword_pathway(self):
        if self.key not in test_data:
            raise KeyError(f"Missing key -- {self.key}:")

    def test_keyword_pathway_value(self):
        assert type(test_data.get(self.key)) is str
        
class TestKeywordVersion:
    '''Test that we have the version keywork and it is of type float'''
    key = "version"
            
    def test_keyword_pathway(self):
        if self.key not in test_data:
            raise KeyError(f"Missing key -- {self.key}:")

    def test_keyword_pathway_value(self):
        assert type(test_data.get(self.key)) is float
        
class TestKeywordSteps:
    '''Test that we have the version steps and it is of type dictionary'''
    key = "steps"
            
    def test_keyword_pathway(self):
        if self.key not in test_data:
            raise KeyError(f"Missing key -- {self.key}:")

    def test_keyword_pathway_value(self):
        assert type(test_data.get(self.key)) is dict

if __name__ == "__main__":
    try_loading()
    TestKeywordPathway.test_keyword_pathway()
    TestKeywordPathway.test_keyword_pathway_value()
    TestKeywordVersion.test_keyword_pathway()
    TestKeywordVersion.test_keyword_pathway_value()
    TestKeywordSteps.test_keyword_pathway()
    TestKeywordSteps.test_keyword_pathway_value()
