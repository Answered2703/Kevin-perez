lista_vacia = []
lista_mas_cinco = [1, 2, 3, 4, 5, 6, 7]

longitud_lista_mas_cinco = len(lista_mas_cinco)
print("Longitud de la lista con más de 5 elementos:", longitud_lista_mas_cinco)


primer_elemento, elemento_central, ultimo_elemento = lista_mas_cinco[0], lista_mas_cinco[len(lista_mas_cinco) // 2], lista_mas_cinco[-1]
print("Primer elemento:", primer_elemento)
print("Elemento central:", elemento_central)
print("Último elemento:", ultimo_elemento)

tipos_datos_mezclados = ["Kevin", 20, 1.71, "soltero", "Villa Zuldany"]
print("Lista de tipos de datos mezclados:", tipos_datos_mezclados)

it_companies = ["Facebook","Google","Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
empresa_existente = "Google" in it_companies
print("Lista de empresas de TI:", it_companies)
print("¿Google está en la lista de empresas de TI?", empresa_existente)

it_companies.insert(1, "Nvidia")
it_companies.sort()
it_companies.reverse()
primer_empresa = it_companies.pop(0)
print("Primera empresa eliminada:", primer_empresa)
it_companies.clear()


