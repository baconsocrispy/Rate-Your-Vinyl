from django.db import models

Villager_Choices = [
    ('Admiral', 'Admiral'), ('Agent S', 'Agent S'), ('Agnes', 'Agnes'),
    ('Al', 'Al'), ('Alfonso', 'Alfonso'), ('Alice', 'Alice'), ('Alli', 'Alli'),
    ('Amelia', 'Amelia'), ('Anabelle', 'Anabelle'), ('Anchovy', 'Anchovy'), ('Angus', 'Angus'),
    ('Anicotti', 'Anicotti'), ('Ankha', 'Ankha'), ('Annalisa', 'Annalisa'),
    ('Annalise', 'Annalise'), ('Antonio', 'Antonio'), ('Apollo', 'Apollo'), ('Apple', 'Apple'),
    ('Astrid', 'Astrid'), ('Audie', 'Audie'), ('Aurora', 'Aurora'), ('Ava', 'Ava'),
    ('Avery', 'Avery'), ('Axel', 'Axel'), ('Baabara', 'Baabara'), ('Bam', 'Bam'),
    ('Bangle', 'Bangle'), ('Barold', 'Barold'), ('Bea', 'Bea'), ('Beardo', 'Beardo'),
    ('Beau', 'Beau'), ('Becky', 'Becky'), ('Bella', 'Bella'), ('Benedict', 'Benedict'),
    ('Benjamin', 'Benjamin'), ('Bertha', 'Bertha'), ('Bettina', 'Bettina'), ('Bianca', 'Bianca'),
    ('Biff', 'Biff'), ('Big Top', 'Big Top'), ('Bill', 'Bill'), ('Biskit', 'Biskit'),
    ('Bitty', 'Bitty'), ('Blaire', 'Blaire'), ('Blanche', 'Blanche'), ('Bluebear', 'Bluebear'),
    ('Bob', 'Bob'), ('Bonbon', 'Bonbon'), ('Bones', 'Bones'), ('Boomer', 'Boomer'), ('Boone', 'Boone'),
    ('Boots', 'Boots'), ('Boris', 'Boris'), ('Boyd', 'Boyd'), ('Bree', 'Bree'), ('Broccolo', 'Broccolo'),
    ('Broffina', 'Broffina'), ('Bruce', 'Bruce'), ('Bubbles', 'Bubbles'), ('Buck', 'Buck'),
    ('Bud', 'Bud'), ('Bunnie', 'Bunnie'), ('Butch', 'Butch'), ('Buzz', 'Buzz'), ('Cally', 'Cally'),
    ('Camofrog', 'Camofrog'), ('Canberra', 'Canberra'), ('Candi', 'Candi'), ('Carmen', 'Carmen'),
    ('Caroline', 'Caroline'), ('Carrie', 'Carrie'), ('Cashmere', 'Cashmere'), ('Celia', 'Celia'),
    ('Cesar', 'Cesar'), ('Chadder', 'Chadder'), ('Chai', 'Chai'), ('Cherry', 'Cherry'),
    ('Chester', 'Chester'), ('Chevre', 'Chevre'), ('Chief', 'Chief'), ('Chops', 'Chops'),
    ('Chow', 'Chow'), ('Chrissy', 'Chrissy'), ('Claude', 'Claude'), ('Claudia', 'Claudia'),
    ('Clay', 'Clay'), ('Cleo', 'Cleo'), ('Clyde', 'Clyde'), ('Coach', 'Coach'), ('Cobb', 'Cobb'),
    ('Coco', 'Coco'), ('Cole', 'Cole'), ('Colton', 'Colton'), ('Cookie', 'Cookie'),
    ('Cousteau', 'Cousteau'), ('Cranston', 'Cranston'), ('Croque', 'Croque'), ('Cube', 'Cube'),
    ('Curlos', 'Curlos'), ('Curly', 'Curly'), ('Curt', 'Curt'),  ('Cyd', 'Cyd'), ('Cyrano', 'Cyrano'),
    ('Daisy', 'Daisy'), ('Deena', 'Deena'), ('Dierdre', 'Dierdre'), ('Del', 'Del'), ('Deli', 'Deli'),
    ('Derwin', 'Derwin'), ('Diana', 'Diana'), ('Diva', 'Diva'), ('Dizzy', 'Dizzy'), ('Dobie', 'Dobie'),
    ('Doc', 'Doc'), ('Dom', 'Dom'), ('Dora', 'Dora'), ('Dotty', 'Dotty'), ('Drago', 'Drago'),
    ('Drake', 'Drake'), ('Drift', 'Drift'), ('Ed', 'Ed'), ('Egbert', 'Egbert'), ('Elise', 'Elise'),
    ('Ellie', 'Ellie'), ('Elmer', 'Elmer'), ('Eloise', 'Eloise'), ('Elvis', 'Elvis'),
    ('Erik', 'Erik'), ('Etoile', 'Etoile'), ('Eugene', 'Eugene'), ('Eunice', 'Eunice'),
    ('Fang', 'Fang'), ('Fauna', 'Fauna'), ('Felicity', 'Felicity'), ('Filbert', 'Filbert'),
    ('Flip', 'Flip'), ('Flo', 'Flo'), ('Flora', 'Flora'), ('Flurry', 'Flurry'),
    ('Francine', 'Francine'), ('Frank', 'Frank'), ('Freckles', 'Freckles'), ('Freya', 'Freya'),
    ('Friga', 'Friga'), ('Frita', 'Frita'), ('Frobert', 'Frobert'), ('Fuchsia', 'Fuchsia'),
    ('Gabi', 'Gabi'), ('Gala', 'Gala'), ('Gaston', 'Gaston'), ('Gayle', 'Gayle'), ('Genji', 'Genji'),
    ('Gigi', 'Gigi'), ('Gladys', 'Gladys'), ('Gloria', 'Gloria'), ('Goldie', 'Goldie'),
    ('Gonzo', 'Gonzo'), ('Goose', 'Goose'), ('Graham', 'Graham'), ('Greta', 'Greta'),
    ('Grizzly', 'Grizzly'), ('Groucho', 'Groucho'), ('Gruff', 'Gruff'), ('Gwen', 'Gwen'),
    ('Hamlet', 'Hamlet'), ('Hamphrey', 'Hamphrey'), ('Hans', 'Hans'), ('Harry', 'Harry'),
    ('Hazel', 'Hazel'), ('Henry', 'Henry'), ('Hippeux', 'Hippeux'), ('Hopkins', 'Hopkins'),
    ('Hopper', 'Hopper'), ('Hornsby', 'Hornsby'), ('Huck', 'Huck'), ('Hugh', 'Hugh'),
    ('Iggly', 'Iggly'), ('Ike', 'Ike'), ('Jacob', 'Jacob'), ('Jacques', 'Jacques'),
    ('Jambette', 'Jambette'), ('Jitters', 'Jitters'), ('Joey', 'Joey'), ('Judy', 'Judy'),
    ('Julia', 'Julia'), ('Julian', 'Julian'), ('June', 'June'), ('Kabuki', 'Kabuki'),
    ('Katt', 'Katt'), ('Keaton', 'Keaton'), ('Ken', 'Ken'), ('Ketchup', 'Ketchup'),
    ('Kevin', 'Kevin'), ('Kid Cat', 'Kid Cat'), ('Kidd', 'Kidd'), ('Kiki', 'Kiki'), ('Kitt', 'Kitt'),
    ('Kitty', 'Kitty'), ('Klaus', 'Klaus'), ('Knox', 'Knox'), ('Kody', 'Kody'), ('Kyle', 'Kyle'),
    ('Leonardo', 'Leonardo'), ('Leopold', 'Leopold'), ('Lily', 'Lily'), ('Limberg', 'Limberg'),
    ('Lionel', 'Lionel'), ('Lobo', 'Lobo'), ('Lolly', 'Lolly'), ('Lopez', 'Lopez'), ('Louie', 'Louie'),
    ('Lucha', 'Lucha'), ('Lucky', 'Lucky'), ('Lucy', 'Lucy'), ('Lyman', 'Lyman'), ('Mac', 'Mac'),
    ('Maddie', 'Maddie'), ('Maelle', 'Maelle'), ('Maggie', 'Maggie'), ('Mallary', 'Mallary'),
    ('Maple', 'Maple'), ('Marcel', 'Marcel'), ('Margie', 'Margie'), ('Marina', 'Marina'),
    ('Marshal', 'Marshal'), ('Marty', 'Marty'), ('Mathilda', 'Mathilda'), ('Megan', 'Megan'),
    ('Melba', 'Melba'), ('Merengue', 'Merengue'), ('Merry', 'Merry'), ('Midge', 'Midge'),
    ('Mint', 'Mint'), ('Mira', 'Mira'), ('Miranda', 'Miranda'), ('Mitzi', 'Mitzi'), ('Moe', 'Moe'),
    ('Molly', 'Molly'), ('Monique', 'Monique'), ('Monty', 'Monty'), ('Moose', 'Moose'),
    ('Mott', 'Mott'), ('Muffy', 'Muffy'), ('Murphy', 'Murphy'), ('Nan', 'Nan'), ('Nana', 'Nana'),
    ('Naomi', 'Naomi'), ('Nate', 'Nate'), ('Nibbles', 'Nibbles'), ('Norma', 'Norma'),
    ('Octavian', 'Octavian'), ('O\'Hare', 'O\'Hare'), ('Olaf', 'Olaf'), ('Olive', 'Olive'),
    ('Olivia', 'Olivia'), ('Opal', 'Opal'), ('Ozzie', 'Ozzie'), ('Pancetti', 'Pancetti'),
    ('Pango', 'Pango'), ('Paolo', 'Paolo'), ('Papi', 'Papi'), ('Pashmina', 'Pashmina'),
    ('Pate', 'Pate'), ('Patty', 'Patty'), ('Paula', 'Paula'), ('Peaches', 'Peaches'),
    ('Peanut', 'Peanut'), ('Pecan', 'Pecan'), ('Peck', 'Peck'),  ('Peewee', 'Peewee'),
    ('Peggy', 'Peggy'), ('Pekoe', 'Pekoe'), ('Penelope', 'Penelope'), ('Phil', 'Phil'),
    ('Phoebe', 'Phoebe'), ('Pierce', 'Pierce'), ('Pietro', 'Pietro'), ('Pinky', 'Pinky'),
    ('Piper', 'Piper'), ('Pippy', 'Pippy'), ('Plucky', 'Plucky'), ('Pompom', 'Pompom'),
    ('Poncho', 'Poncho'), ('Poppy', 'Poppy'), ('Portia', 'Portia'), ('Prince', 'Prince'),
    ('Puck', 'Puck'), ('Puddles', 'Puddles'), ('Pudge', 'Pudge'), ('Punchy', 'Punchy'),
    ('Purrl', 'Purrl'), ('Queenie', 'Queenie'), ('Quillson', 'Quillson'), ('Raddle', 'Raddle'),
    ('Rasher', 'Rasher'), ('Raymond', 'Raymond'), ('Renee', 'Renee'), ('Reneigh', 'Reneigh'),
    ('Rex', 'Rex'), ('Rhonda', 'Rhonda'), ('Ribbot', 'Ribbot'), ('Ricky', 'Ricky'), ('Rilla', 'Rilla'),
    ('Rizzo', 'Rizzo'), ('Roald', 'Roald'), ('Robin', 'Robin'), ('Rocco', 'Rocco'),
    ('Rocket', 'Rocket'), ('Rod', 'Rod'), ('Rodeo', 'Rodeo'), ('Rodney', 'Rodney'), ('Rolf', 'Rolf'),
    ('Rooney', 'Rooney'), ('Rory', 'Rory'), ('Roscoe', 'Roscoe'), ('Rosie', 'Rosie'),('Rowan', 'Rowan'),
    ('Ruby', 'Ruby'), ('Rudy', 'Rudy'), ('Sally', 'Sally'), ('Samson', 'Samson'), ('Sandy', 'Sandy'),
    ('Savannah', 'Savannah'), ('Scoot', 'Scoot'), ('Shari', 'Shari'), ('Sheldon', 'Sheldon'),
    ('Shep', 'Shep'), ('Sherb', 'Sherb'), ('Simon', 'Simon'), ('Skye', 'Skye'), ('Sly', 'Sly'),
    ('Snake', 'Snake'), ('Snooty', 'Snooty'), ('Soleil', 'Soleil'), ('Sparro', 'Sparro'),
    ('Spike', 'Spike'), ('Spork', 'Spork'), ('Sprinkle', 'Sprinkle'), ('Sprocket', 'Sprocket'),
    ('Static', 'Static'), ('Stella', 'Stella'), ('Sterling', 'Sterling'), ('Stinky', 'Stinky'),
    ('Stitches', 'Stitches'), ('Stu', 'Stu'), ('Sydney', 'Sydney'), ('Sylvana', 'Sylvana'),
    ('Sylvia', 'Sylvia'), ('Tabby', 'Tabby'), ('Tad', 'Tad'), ('Tammi', 'Tammi'), ('Tammy', 'Tammy'),
    ('Tangy', 'Tangy'), ('Tank', 'Tank'), ('Tasha', 'Tasha'), ('T-Bone', 'T-Bone'), ('Teddy', 'Teddy'),
    ('Tex', 'Tex'), ('Tia', 'Tia'), ('Tiffany', 'Tiffany'), ('Timbra', 'Timbra'), ('Tipper', 'Tipper'),
    ('Toby', 'Toby'), ('Tom', 'Tom'), ('Truffles', 'Truffles'), ('Tucker', 'Tucker'), ('Tutu', 'Tutu'),
    ('Twiggy', 'Twiggy'), ('Tybalt', 'Tybalt'), ('Ursala', 'Ursala'), ('Vesta', 'Vesta'), ('Vic', 'Vic'),
    ('Victoria', 'Victoria'), ('Violet', 'Violet'), ('Vivian', 'Vivian'), ('Vladimir', 'Vladimir'),
    ('Wade', 'Wade'), ('Walker', 'Walker'), ('Walt', 'Walt'), ('Wart Jr.', 'Wart Jr.'),
    ('Weber', 'Weber'), ('Wendy', 'Wendy'), ('Whitney', 'Whitney'), ('Willow', 'Willow'),
    ('Winnie', 'Winnie'), ('Wolfgang', 'Wolfgang'), ('Yuka', 'Yuka'), ('Zell', 'Zell'),
    ('Zucker', 'Zucker'),
]


class Account(models.Model):
    first_name = models.CharField(max_length=60, default='', blank=False, null=False)
    last_name = models.CharField(max_length=60, default='', blank=False, null=False)
    username = models.CharField(max_length=60, default='', blank=False, null=False)
    password = models.CharField(max_length=60, default='', blank=False, null=False)
    island_name = models.CharField(max_length=60, default='', blank=False, null=False)
    villager_1 = models.CharField(max_length=20, choices=Villager_Choices, blank=True, null=True)
    villager_2 = models.CharField(max_length=20, choices=Villager_Choices, blank=True, null=True)
    villager_3 = models.CharField(max_length=20, choices=Villager_Choices, blank=True, null=True)
    villager_4 = models.CharField(max_length=20, choices=Villager_Choices, blank=True, null=True)
    villager_5 = models.CharField(max_length=20, choices=Villager_Choices, blank=True, null=True)
    villager_6 = models.CharField(max_length=20, choices=Villager_Choices, blank=True, null=True)
    villager_7 = models.CharField(max_length=20, choices=Villager_Choices, blank=True, null=True)
    villager_8 = models.CharField(max_length=20, choices=Villager_Choices, blank=True, null=True)
    villager_9 = models.CharField(max_length=20, choices=Villager_Choices, blank=True, null=True)
    villager_10 = models.CharField(max_length=20, choices=Villager_Choices, blank=True, null=True)

    Accounts = models.Manager()


    def __str__(self):
        return self.username