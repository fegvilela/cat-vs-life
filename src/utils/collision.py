def check_collision(player, enemies, attack_type):
    hits = pygame.sprite.spritecollide(player, enemies, False)
    for enemy in hits:
        player.hp -= enemy.damage
        print(f"Cat HP: {player.hp}")

def check_attack(attacks, enemies):
    for attack in attacks:
        hits = pygame.sprite.spritecollide(attack, enemies, False)
        for enemy in hits:
            enemy.hp -= attack.damage
            if enemy.hp <= 0:
                enemy.kill()
