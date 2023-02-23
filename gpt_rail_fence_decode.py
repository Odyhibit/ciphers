def build_rails(cipher, rails, offset=0):
    period: int = 2 * (rails - 1)
    index = offset
    rail_fence = [[] for _ in range(rails)]
    for row in range(rails):
        for i in range(len(cipher)):
            if i % period == row:
                rail_fence[row].append(cipher[index])
                index += 1
            elif period - (i % period) == row:
                rail_fence[row].append(cipher[index])
                index += 1
    print(cipher)
    for rail in rail_fence:
        print(rail)

def decode(cipher,rails,offset):
    pass




ciphertext = 'T_te_ept_t_tiu__thssnec_sa_xml_etta_sjs_en_sdfrtsigieninaexhiubgeoen'

print(build_rails(ciphertext, 3))
