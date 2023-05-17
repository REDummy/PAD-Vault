def penguranganSatuan(jumlah, satuan):
    result = []
    gelas = int()
    sdm = int()
    sdt  = int()
    if satuan == "gelas":
        gelas = jumlah
    elif satuan == "sendok makan":
        gelas = jumlah // 16
        sdm = jumlah % 16
    elif satuan == "sendok teh":
        gelas = jumlah // 48 # 1 gelas = 16 sdm = 48 sendok teh
        sdm = (jumlah % 48) // 3 # 1 sendok makan = 3 sendok teh
        sdt = jumlah % 3
    else:
        return "Satuan yang diberikan tidak valid."

    if gelas > 0:
        result.append(f"{gelas} gelas")
    if sdm > 0:
        result.append(f"{sdm} sendok makan")
    if sdt > 0:
        result.append(f"{sdt} sendok teh")
        
    return f"{jumlah} {satuan} = {', '.join(result)}"

print(penguranganSatuan(59, "sendok teh")) 
print(penguranganSatuan(95, "sendok teh")) 
print(penguranganSatuan(33, "sendok makan")) 
print(penguranganSatuan(100, "sendok teh")) 
print(penguranganSatuan(4, "gelas"))
