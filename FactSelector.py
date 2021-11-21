import random

class FactSelector:
    list_of_facts = []

    def __init__(self):
        self.list_of_facts = ["When more than one ninja champion is in the same team, they lose 1 health.",
                              "When Sion kills Zyra and vice versa, they get 2 bonus gold.",
                              "Also Yorick’s ghouls will target Zyra’s plants if in range.",
                              "Graves and Nocturne have a unique dialogue toward each other.",
                              "Malphite’s ground slam leaves Riot Games logo on the ground.",
                              "Vilemaw will perform a special dance if two other champions dance near him.",
                              "Maokai is an anagram of I am oak.",
                              "Maokai and Zyra get 1 movement speed when they are near each other.",
                              "Spirit Guard Udyr has special taunts against Nidalee in cougar form, Anivia, Volibear and Rammus.",
                              "Ashe has special taunts against Sejuani and Lissandra.",
                              "Lissandra has a special monologue in ARAM.",
                              "Lissandra has a special monologue in ARAM.",
                              "Tryndamere and Aatrox have a special interaction.",
                              "When Zilean and Volibear are on 2 separate teams, Volibear gets the chronokeeper hater buff and Zilean gets the armoured bear hater buff.",
                              "If you walk into a bush as Skarner and wait for a bit, he will say “Skar Skar Skarner” as a reference to Pokemon.",
                              "If Jinx or Vi perform their special taunt on Caitlyn, she’ll get the debuff “Agitated”.",
                              "Whenever Jinx is on an opposing team to Caitlyn and/or Vi, they each get a debuff titled “catch me if you can”.",
                              "When Vi and Caitlyn score a kill together, they receive 1 extra gold.",
                              "Leona does 1 less damage with her Sunlight to champions with sunglasses.",
                              "Nidalee featured a hidden passive prior to her rework that granted nearby allied champions 5 experience every 5 seconds if they were lower level than Nidalee.",
                              "When Zyra’s hit by Leona’s sunlight, she and her plants grow slightly.",
                              "When Zyra’s hit by Leona’s sunlight, she and her plants grow slightly.",
                              "When Zyra’s hit by Leona’s sunlight, she and her plants grow slightly.",
                              "When Zyra’s hit by Leona’s sunlight, she and her plants grow slightly.",
                              "Sejuani’s dash also breaks through Anivia’s wall.",
                              "When an enemy Nunu dies near Thresh, two souls drop, one for Nunu and other for Willump (the yeti).",
                              "If Volibear’s frenzy (active effect) deals a killing blow against Lollipoppy, he’ll have a lollipop in his mouth for the rest of the match.",
                              "Heimer’s passive heals turrets."]

    def get_fact(self):
        return random.choice(self.list_of_facts)
