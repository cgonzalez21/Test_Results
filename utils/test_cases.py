def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Blocker', 'when user goes to main page, page should be loaded'],
    ['Blocker', 'In Main page, when user scrool to the footer, should see the footer first description'],
    ['Blocker', 'In Main page, when user scrool to the footer, should see the footer second description'],
    ['Blocker', 'In Main page, when user scrool to the footer, should see the Contact Us button'],
    ['Blocker', 'In Main page, when user scrool to the footer, should see the FAQ button'],
    ['Blocker', 'In Main page, when user scrool to the footer, should see the Terms of Use button'],
    ['Blocker', 'In Main page, when user scrool to the footer, should see the Privacy Policy button'],
    ['Blocker', 'In Main page, when user scrool to the footer, should see the CA Privacy Notice button'],
    ['Blocker', 'In Find My Match Section, when user type a valid zip code, he should see Find my match box'],
    ['Blocker', 'User is seing the Recall news, when he/she share it via twitter'],
    ['Blocker', 'User is seing the Recall news, when he/she share it via facebook'],
    ['Blocker', 'User is seing the first listed in Related News'],
    ['Blocker', 'User is seing the lasted listed in Related News'],
]
