import pygame
import fonctions as f 
import cartes as c 

def motion(window,deck,white): # Permet de lever les cartes losrqu'on passe la souris dessus
    
    
    for carte in deck : # On parcourt la main
        
        
        # Ici on dessine un rectantgle qui correspond à la carte pour pouvoir gerer notre évenment 
        rectangle = pygame.draw.rect(window,white,(carte.position_x , carte.position_y , 187 - 107 , 260))
        # On réaffiche la carte par dessus le rectangle de selection 
        window.blit(carte.image,(carte.position_x  , carte.position_y))
        
        if rectangle.collidepoint(pygame.mouse.get_pos()) == True and carte.selected == False : # On regarde si la souris est dans le rectangle de la carte 
            
            window.blit(carte.image,(carte.position_x , carte.position_y - 50)) # On repositionne la carte
            pygame.draw.rect(window,white,(carte.position_x , carte.position_y - 50 + 260 , 187  , 50)) # On redessine un rectangle blanc en dessous de la carte
            
            carte.motion = True
      
            
        if pygame.mouse.get_pressed()[0] == 1 and carte.motion == True and carte.selected == False:
            carte.selected = True
            print(carte.selected)
            window.blit(carte.image,(carte.position_x , carte.position_y - 50))
            pygame.draw.rect(window,white,(carte.position_x , carte.position_y - 50 + 260 , 187  , 50))
            
        
         
            
    # if carte.selected == True and carte.motion == True :

        
			    
                
            

        
        
        

            
            