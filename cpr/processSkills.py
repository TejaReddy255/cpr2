def processSkillsFunct(allSkills):
    completedSkills = {}

    for skill in allSkills:
        if skill in completedSkills.keys():
            pass
        else:
            completedSkills[skill] = 1
