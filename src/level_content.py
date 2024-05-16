from level_db import Session, LevelPageContent

def add_level_content_to_database():
    session = Session()
    session.query(LevelPageContent).delete()

    # Add content to the database
    content_entries = [
        LevelPageContent(
            question='What does WiFi stand for?',
            answer='wireless fidelity',
            requires_input=1
        ),
        LevelPageContent(
            question='What type of attack involves setting up an unauthorized wireless access point on a wired enterprise network?',
            option1='Rogue AP',
            option2='MitM',
            option3='DoS',
            option4='XSS',
            answer='Rogue AP',
            requires_input=0
        ),
        LevelPageContent(
            question='What protocol is exploited in ARP spoofing attacks to associate a MAC address with a false IP address?',
            option1='TCP',
            option2='IPSec',
            option3='ARP',
            option4='HTTP',
            answer='ARP',
            requires_input=0
        ),
        LevelPageContent(
            question='Full Form of MitM',
            answer='Man in the Middle',
            requires_input=1
        ),
        LevelPageContent(
            question='Which encryption protocol is recommended to secure WiFi communications?',
            option1='WEP',
            option2='WPA',
            option3='WPA2 or WPA3',
            option4='WPS',
            answer='WPA2 or WPA3',
            requires_input=0
        )
    ]

    for entry in content_entries:
        session.add(entry)

    session.commit()

    session.close()