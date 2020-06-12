import skillBasedMatch

import unittest

class TestSkillBasedMatch(unittest.TestCase) : 
    def test_validate_team_size(self) :
        self.assertRaises(ValueError, skillBasedMatch.checkTeamSize, 0)
        self.assertRaises(ValueError, skillBasedMatch.checkTeamSize, -1)

    def test_validate_number_of_players(self) :
        self.assertRaises(ValueError, skillBasedMatch.validateInputs, 2, 3)
        self.assertRaises(ValueError, skillBasedMatch.validateInputs, 2, 5)
        self.assertRaises(ValueError, skillBasedMatch.validateInputs, 2, 6)
        self.assertRaises(ValueError, skillBasedMatch.validateInputs, 3, 6)
    
    def test_possible_teams(self) :
        self.assertEqual(
            skillBasedMatch.getAllPossibleTeams(4, 2, [['bleh', '85'], ['Aequitas', '90'], ['akS', '87'], ['lamiV', '20']]), 
            {'akS,lamiV': 53.5, 'Aequitas,lamiV': 55.0, 'Aequitas,akS': 88.5, 'bleh,lamiV': 52.5, 'bleh,akS': 86.0, 'bleh,Aequitas': 87.5}
        )

        self.assertEqual(
            skillBasedMatch.getAllPossibleTeams(4, 2, [['Wizard', '63'], ['Pro', '80'], ['Noob', '23'], ['Memer', '89']]), 
            {'Noob,Memer': 56.0, 'Pro,Memer': 84.5, 'Pro,Noob': 51.5, 'Wizard,Memer': 76.0, 'Wizard,Noob': 43.0, 'Wizard,Pro': 71.5}
        )

        self.assertEqual(
            skillBasedMatch.getAllPossibleTeams(6, 3, [['a', '23'], ['b', '45'], ['c', '30'], ['d', '19'], ['e', '22'], ['f', '16']]),
            {'d,e,f': 19.0, 'c,e,f': 22.666666666666664, 'c,d,f': 21.666666666666664, 'c,d,e': 23.666666666666664, 'b,e,f': 27.666666666666664, 'b,d,f': 26.666666666666664, 'b,d,e': 28.666666666666664, 'b,c,f': 30.333333333333332, 'b,c,e': 32.333333333333336, 'b,c,d': 31.333333333333332, 'a,e,f': 20.333333333333332, 'a,d,f': 19.333333333333332, 'a,d,e': 21.333333333333332, 'a,c,f': 23.0, 'a,c,e': 25.0, 'a,c,d': 24.0, 'a,b,f': 28.0, 'a,b,e': 30.0, 'a,b,d': 29.0, 'a,b,c': 32.66666666666667}
        )

        self.assertEqual(
            skillBasedMatch.getAllPossibleTeams(2, 1, [['as', '60'], ['ak', '50']]),
            {'as': 60, 'ak': 50}
        )


if __name__ == '__main__' :
    unittest.main()
