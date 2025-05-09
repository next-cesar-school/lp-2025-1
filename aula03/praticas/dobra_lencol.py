def dobra_lencol(gaveta, lencol):
    if lencol <= gaveta:
        return 0
    else:
        print(f'Precisa dobrar! {lencol/2}')
        return 1 + dobra_lencol(gaveta, lencol/2)

#print(dobra_lencol(4, 2))
#print(dobra_lencol(2, 4))
print(dobra_lencol(2, 80))
