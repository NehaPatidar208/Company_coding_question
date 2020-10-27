def functionSanto(product,sequence):
    cof=['Espresso Coffee','Cappuccino Coffee','Latte Coffee']
    tea=['Plain Tea','Assam Tea','Ginger Tea','Cardamom Tea','Masala Tea','Lemmon Tea','Green Tea','Organic Darjeeling Tea']
    soup=['Hot and Sour Soup','vcs','tmt','stc']
    bvg=['sdg','bd','bpd']
    if product == 'c' and sequence < len(cof):
        print("Welcome to CCD")
        print("Enjoy your",cof[sequence])
    if product == 't' and sequence <len(tea):
            print("Welcome to CCD")
            print("Enjoy your",tea[sequence])
    if product == 's'and sequence <len(tea):
        print("Welcome to CCD")
        print("Enjoy your",soup[sequence])
        
    if product == 'b'and sequence <len(bvg):
        print("Welcome to CCD")
        print("Enjoy your",bvg[sequence])
    else:
        print("INVALID OPTION!")
main_menu=input()
sub_menu=int(input())
functionSanto(main_menu,sub_menu)
