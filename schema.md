# Nombre de la organización: 
Agencia Nacional de Defensa Jurídica del Estado
# Persona de contacto:
* Jorge Mario Carrasco Ortiz
* Cel 3103234747
* Correo jorge.carrasco@defensajuridica.gov.co
# Se debe solicitar (Non-disclosure agreement - NDA)


# Tabla REPORTE_LAUDOS

Permite al usuario descargar la información de los laudor (procesos arbitrales terminados) de todas las entidades registradas en el sistema. Los siguientes son los campos que incluye este reporte:

|     | Columna                                                              | Descripción                                                          | Tipo           |
|----:|:---------------------------------------------------------------------|:---------------------------------------------------------------------|:---------------|
|   0 | ID_de_la_entidad                                                     | Código de la entidad                                                                  | object         |
|   1 | Condena_indexada_favor                                               | Valor de condena indexada (AFAVOR - Convocante)                                                             | float64        |
|   2 | Condena_indexada                                                     | Valor de condena indexada (ENCONTRA - Convocado)                                                                             | float64        |
|   3 | Pretension_indexada                                                  | Valor de la prentesiòn indexada                                                                  | float64        |                             | int64          |
|   5 | UNMO_DESCRIPCION_PRETEN                                              | Unidades monetarias en la indexación                                                                  | object         |
|   6 | valor_inicial_a_indexar                                              | Valor de la pretensiones a indexar                                                                  | float64        |
|   7 | ESTADO_FIN                                                           | Estado del arbitramento                                                                  | object         |
|   8 | contraparte                                                          | Contraparte del proceso                                                                  | object         |
|   9 | cont_convocados                                                      | Contraperte convocados                                                                  | object         |
|  10 | cont_convocantes                                                     | Contraperte convocantes                                                                  | object         |                             | object         |
|  12 | ID_ARB                                                               | ID_ARB                                                               | object         |
|  13 | EXTRAE                                                               | EXTRAE                                                               | object         |
|  14 | par__entidad                                                         | par_ entidad                                                         | object         |
|  15 | CONSECUTIVO                                                          | CONSECUTIVO                                                          | object         |
|  16 | CONTADOR_CASOS                                                       | CONTADOR CASOS                                                       | object         |
|  17 | Es_demanda_de_Reconvencion_(R_/VACIO)                                | Es demanda de Reconvención (R /VACIO)                                | object         |
|  18 | Es_interinstitucional                                                | Es interinstitucional                                                | object         |
|  19 | Fecha_de_Registro_en_la_base_                                        | Fecha de Registro en la base                                         | object         |
|  20 | orfeo_no.                                                            | orfeo no.                                                            | object         |
|  21 | Notificado__por:_Centro_de_arbitramento_(Fecha)_                     | Notificado  por: Centro de arbitramento (Fecha)                      | object         |
|  22 | Notificado_por:_Entidad_(fecha)                                      | Notificado por: Entidad (fecha)                                      | object         |
|  23 | Entrega_de_Laudo_Arbitral_(fecha)                                    | Entrega de Laudo Arbitral (fecha)                                    | object         |
|  24 | Informe__trimestral_(fecha)_                                         | Informe  trimestral (fecha)                                          | object         |
|  25 | Ultima_fecha_de_actualizacion_Base                                   | Ultima fecha de actualización Base                                   | object         |
|  26 | ENTIDADES_VINCULADAS                                                 | ENTIDADES VINCULADAS                                                 | object         |
|  27 | NIT                                                                  | NIT                                                                  | object         |
|  28 | NACIONAL/_TERRITORIAL/INTERNACIONAL                                  | NACIONAL/ TERRITORIAL/INTERNACIONAL                                  | object         |
|  29 | CALIDAD_EN_LA_QUE_ACTUA_LA_ENTIDAD                                   | CALIDAD EN LA QUE ACTÚA LA ENTIDAD                                   | object         |
|  30 | TIPO_DE_ARBITRAMENTO                                                 | TIPO DE ARBITRAMENTO                                                 | object         |
|  31 | Ndeg_de_expediente_Camara_de_Comercio_                               | N° de expediente Cámara de Comercio                                  | object         |
|  32 | NOMBRE_CENTRO_DE_ARBITRAJE                                           | NOMBRE CENTRO DE ARBITRAJE                                           | object         |
|  33 | NUMERO_DE_CONTRATO                                                   | NÚMERO DE CONTRATO                                                   | object         |
|  34 | ANO_DE_CONTRATO                                                      | AÑO DE CONTRATO                                                      | object         |
|  35 | TIPO_DE_CONTRATO                                                     | TIPO DE CONTRATO                                                     | object         |
|  36 | ES_DE_INFRAESTRUCTURA                                                | ES DE INFRAESTRUCTURA                                                | object         |
|  37 | Auto_admisorio                                                       | Auto admisorio                                                       | object         |
|  38 | Demanda                                                              | Demanda                                                              | object         |
|  39 | Instalacion_del_Arbitramento._                                       | Instalacion del Arbitramento.                                        | object         |
|  40 | Contestacion_demanda                                                 | Contestación demanda                                                 | object         |
|  41 | Demanda_de_Reconvencion                                              | Demanda de Reconvención                                              | object         |
|  42 | Laudo_Arbitral                                                       | Laudo Arbitral                                                       | object         |
|  43 | Otros_anexos                                                         | Otros anexos                                                         | object         |
|  44 | pieza_arbitral?                                                      | pieza arbitral?                                                      | object         |
|  45 | FECHA_DE_ADMISION_DEL_CASO                                           | FECHA DE ADMISIÓN DEL CASO                                           | object         |
|  46 | HECHOS                                                               | HECHOS                                                               | object         |
|  47 | MUNICIPIO_DE_LOS_HECHOS                                              | MUNICIPIO DE LOS HECHOS                                              | object         |
|  48 | DEPARTAMENTO_DE_LOS_HECHOS                                           | DEPARTAMENTO DE LOS HECHOS                                           | object         |
|  49 | CAUSA                                                                | CAUSA                                                                | object         |
|  50 | LA_PRETENSION/CUANTIA_ES_DETERMINADA?                                | LA PRETENSIÓN/CUANTÍA ES DETERMINADA?                                | object         |
|  51 | PRETENSION_INICIAL__DEL_CASO                                         | PRETENSIÓN INICIAL  DEL CASO                                         | object         |
|  52 | UNIDAD_MONETARIA_PRETENCION                                          | UNIDAD MONETARIA PRETENCION                                          | object         |
|  53 | CUANTIA_INICIAL_DEL_CASO                                             | CUANTIA INICIAL DEL CASO                                             | object         |
|  54 | UNIDAD_MONETARIA_CUANTIA                                             | UNIDAD MONETARIA CUANTIA                                             | object         |
|  55 | VALORACION_ECONOMICA_INICIAL_                                        | VALORACIÓN ECONÓMICA INICIAL                                         | object         |
|  56 | UNIDAD_MONETARIA_VALORACION                                          | UNIDAD MONETARIA VALORACION                                          | object         |
|  57 | VALOR_DE_PROVISION_CONTABLE_EN_CASO_DE_PERDIDA_(PESOS)               | VALOR DE PROVISIÓN CONTABLE EN CASO DE PERDIDA (PESOS)               | object         |
|  58 | VALOR_TOTAL_DE_LA_CUANTIA_(EN_SALARIOS_MINIMOS)                      | VALOR TOTAL DE LA CUANTIA (EN SALARIOS MINIMOS)                      | object         |
|  59 | IMPACTO                                                              | IMPACTO                                                              | object         |
|  60 | PARTICIPA_UNA_ENTIDAD_PUBLICA_COMO_CONVOCANTE?                       | PARTICIPA UNA ENTIDAD PÚBLICA COMO CONVOCANTE?                       | object         |
|  61 | NOMBRE_DE_LA_ENTIDAD_CONVOCANTE                                      | NOMBRE DE LA ENTIDAD CONVOCANTE                                      | object         |
|  62 | NOMBRE_DE_PARTICULARES_CONVOCANTES                                   | NOMBRE DE PARTICULARES CONVOCANTES                                   | object         |
|  63 | TIPO_DE_DOCUMENTO_DE_IDENTIFICACION_DE_PARTICULARES_CONVOCANTES      | TIPO DE DOCUMENTO DE IDENTIFICACIÓN DE PARTICULARES CONVOCANTES      | object         |
|  64 | Ndeg_DE_DOCUMENTO_DE_IDENTIFICACION_DE_PARTICULARES_CONVOCANTES      | N° DE DOCUMENTO DE IDENTIFICACIÓN DE PARTICULARES CONVOCANTES        | object         |
|  65 | TIPO_DE_PERSONA_CONVOCANTE_                                          | TIPO DE PERSONA CONVOCANTE                                           | object         |
|  66 | CALIDAD_                                                             | CALIDAD                                                              | object         |
|  67 | FECHA_DE_DESIGNACION_DEL_APODERADO_ACTUAL_DEL_CONVOCANTE             | FECHA DE DESIGNACIÓN DEL APODERADO ACTUAL DEL CONVOCANTE             | object         |
|  68 | APELLIDOS_Y_NOMBRE_DE_APODERADO_CONVOCANTE_                          | APELLIDOS Y NOMBRE DE APODERADO CONVOCANTE                           | object         |
|  69 | PRIMER_APELLIDO                                                      | PRIMER APELLIDO                                                      | object         |
|  70 | SEGUNDO_APELLIDO                                                     | SEGUNDO APELLIDO                                                     | object         |
|  71 | NOMBRE                                                               | NOMBRE                                                               | object         |
|  72 | TIPODEDOCUMENTODEIDENTIFICACION                                      | TIPODEDOCUMENTODEIDENTIFICACIÓN                                      | object         |
|  73 | Ndeg_DOCUMENTO_DE_IDENTIFICACION                                     | N° DOCUMENTO DE IDENTIFICACIÓN                                       | object         |
|  74 | Ndeg_TARJETA_PROFESIONAL                                             | N° TARJETA PROFESIONAL                                               | object         |
|  75 | PARTICIPA_UNA_ENTIDAD_PUBLICA_COMO_CONVOCADA?                        | PARTICIPA UNA ENTIDAD PÚBLICA COMO CONVOCADA?                        | object         |
|  76 | _NOMBRE_DE_LA_ENTIDAD_CONVOCADA                                      | NOMBRE DE LA ENTIDAD CONVOCADA                                       | object         |
|  77 | NOMBRE_DE_PARTICULARES_CONVOCADOS                                    | NOMBRE DE PARTICULARES CONVOCADOS                                    | object         |
|  78 | TIPO_DE_DOCUMENTO_DE_IDENTIFICACION_DE_PARTICULARES_CONVOCADOS       | TIPO DE DOCUMENTO DE IDENTIFICACIÓN DE PARTICULARES CONVOCADOS       | object         |
|  79 | Ndeg_DE_DOCUMENTO_DE_IDENTIFICACION_DE_PARTICULARES_CONVOCADOS       | N° DE DOCUMENTO DE IDENTIFICACIÓN DE PARTICULARES CONVOCADOS         | object         |
|  80 | CALIDAD_.1                                                           | CALIDAD .1                                                           | object         |
|  81 | APELLIDOS_Y_NOMBRES_DEL_APODERADO-_CONVOCADO                         | APELLIDOS Y NOMBRES DEL APODERADO- CONVOCADO                         | object         |
|  82 | PRIMER_APELLIDO_APODERADO_CONVOCADO                                  | PRIMER APELLIDO_APODERADO CONVOCADO                                  | object         |
|  83 | SEGUNDO_APELLIDO__APODERADO_CONVOCADO                                | SEGUNDO APELLIDO__APODERADO CONVOCADO                                | object         |
|  84 | NOMBRE_APODERADO_CONVOCADO                                           | NOMBRE_APODERADO CONVOCADO                                           | object         |
|  85 | TIPODEDOCUMENTODEIDENTIFICACION_APODERADOCONVOCADO                   | TIPODEDOCUMENTODEIDENTIFICACIÓN_APODERADOCONVOCADO                   | object         |
|  86 | Ndeg_DOCUMENTO_DE_IDENTIFICACION_APODERADO_CONVOCADO_                | N° DOCUMENTO DE IDENTIFICACIÓN_APODERADO CONVOCADO                   | object         |
|  87 | Ndeg_TARJETA_PROFESIONAL.1                                           | N° TARJETA PROFESIONAL.1                                             | object         |
|  88 | FECHA_DE_INSTALACION_DE_LOS_ARBITROS_                                | FECHA DE INSTALACION DE LOS ARBITROS                                 | object         |
|  89 | MECANISMO_DE_SELECCION_DE_LOS_ARBITROS                               | MECANISMO DE SELECCIÓN DE LOS ÁRBITROS                               | object         |
|  90 | ARBITRO_N0.                                                          | ARBITRO N0.                                                          | object         |
|  91 | APELLIDOS_Y_NOMBRE_DE_ARBITRO_                                       | APELLIDOS Y NOMBRE DE ARBITRO                                        | object         |
|  92 | PRIMER_APELLIDO_1                                                    | PRIMER APELLIDO_1                                                    | object         |
|  93 | SEGUNDO_APELLIDO1_1                                                  | SEGUNDO APELLIDO1_1                                                  | object         |
|  94 | NOMBRE_1                                                             | NOMBRE_1                                                             | object         |
|  95 | TIPO_DOCUMENTO_DE_IDENTIFICACION_1                                   | TIPO DOCUMENTO DE IDENTIFICACIÓN_1                                   | object         |
|  96 | CONTADOR_ARBITROS                                                    | CONTADOR ARBITROS                                                    | object         |
|  97 | Ndeg_DOCUMENTO_DE_IDENTIFICACION_1                                   | N° DOCUMENTO DE IDENTIFICACIÓN_1                                     | object         |
|  98 | APELLIDOS_Y_NOMBRE_DEL_SECRETARIO                                    | APELLIDOS Y NOMBRE DEL SECRETARIO                                    | object         |
|  99 | PRIMER_APELLIDO_SECRETARIO                                           | PRIMER APELLIDO_SECRETARIO                                           | object         |
| 100 | SEGUNDO_APELLIDO1_SECRETARIO                                         | SEGUNDO APELLIDO1_SECRETARIO                                         | object         |
| 101 | NOMBRE_SECRETARIO                                                    | NOMBRE_SECRETARIO                                                    | object         |
| 102 | TIPO_DOCUMENTO_DE_IDENTIFICACION_SECRETARIO                          | TIPO DOCUMENTO DE IDENTIFICACIÓN_SECRETARIO                          | object         |
| 103 | NUMERO_DE_IDENTIFICACION_SECRETARIO                                  | NUMERO DE IDENTIFICACIÓN SECRETARIO                                  | object         |
| 104 | ESTADO_DEL_CASO                                                      | ESTADO DEL CASO                                                      | object         |
| 105 | INSTANCIA                                                            | INSTANCIA                                                            | object         |
| 106 | ETAPA                                                                | ETAPA                                                                | object         |
| 107 | ULTIMA_ACTUACION                                                     | ULTIMA ACTUACIÓN                                                     | object         |
| 108 | FECHA_ULTIMA_ACTUACION                                               | FECHA ÚLTIMA ACTUACIÓN                                               | object         |
| 109 | SENTIDO_DEL_LAUDO                                                    | nan                                                                  | object         |
| 110 | FECHA_LAUDO_ARBITRAL                                                 | FECHA LAUDO ARBITRAL                                                 | object         |
| 111 | FECHA_DE_TERMINACION_DEL_TRAMITE_ARBITRAL                            | FECHA DE TERMINACIÓN DEL TRÁMITE ARBITRAL                            | object         |
| 112 | VALOR_DE_LA_CONDENA_EN_CONTRA                                        | VALOR DE LA CONDENA EN CONTRA                                        | object         |
| 113 | UNIDAD_MONETARIA_CONDENA_EN_CONTRA                                   | UNIDAD MONETARIA CONDENA EN CONTRA                                   | object         |
| 114 | VALOR_DE_LA_CONDENA_A_FAVOR                                          | VALOR DE LA CONDENA A FAVOR                                          | object         |
| 115 | UNIDAD_MONETARIA_CONDENA_A_FAVOR                                     | UNIDAD MONETARIA CONDENA A FAVOR                                     | object         |
| 116 | TIPO_DE_CONDENA                                                      | TIPO DE CONDENA                                                      | object         |
| 117 | VALOR_INTERESES_corrientes_y_MORATORIOS_(YA_INCLUIDOS_EN_LA_CONDENA) | VALOR INTERESES corrientes y MORATORIOS (YA INCLUIDOS EN LA CONDENA) | object         |
| 118 | VALOR_GASTOS_DEL_PROCESO_(INCLUYE_AGENCIAS_EN_DERECHO)               | VALOR GASTOS DEL PROCESO (INCLUYE AGENCIAS EN DERECHO)               | object         |
|     | SANCION_ART.206_CGP                                                  | SANCION ART.206 CGP                                                  |                |
| 119 | VALOR_DE_LA_RESOLUCION_DE_PAGO                                       | VALOR DE LA RESOLUCIÓN DE PAGO                                       | object         |
| 120 | FECHA_RESOLUCION_DE_PAGO                                             | FECHA RESOLUCIÓN DE PAGO                                             | object         |
| 121 | VALOR_PAGADO_A_LA_ENTIDAD                                            | VALOR PAGADO A LA ENTIDAD                                            | object         |
| 122 | FECHA_DE_PAGO_A_LA_ENTIDAD                                           | FECHA DE PAGO A LA ENTIDAD                                           | object         |
| 123 | NUMERO_RESOLUCION_DE_PAGO                                            | NÚMERO RESOLUCIÓN DE PAGO                                            | object         |
| 124 | VALOR_DE_INTERESES_PAGADOS                                           | VALOR DE INTERESES PAGADOS                                           | object         |
| 125 | ?SE_INTERPUSO_RECURSO_EXTRAORDINARIO_DE_NULIDAD?                     | ¿SE INTERPUSO RECURSO EXTRAORDINARIO DE NULIDAD?                     | object         |
| 126 | CODIGO_UNICO_DEL_PROCESO_RADICADO_ANTE_LO_CONTENCIOSO_ADMINISTRATIVO | CÓDIGO UNICO DEL PROCESO RADICADO ANTE LO CONTENCIOSO ADMINISTRATIVO | object         |
| 127 | OBSERVACIONES                                                        | OBSERVACIONES                                                        | object         |
| 128 | VALOR_FIJADO_POR_COSTAS_                                             | VALOR FIJADO POR COSTAS                                              | object         |
| 129 | UNIDAD_MONETARIA                                                     | UNIDAD MONETARIA                                                     | object         |
| 130 | COSTAS_A_FAVOR_O_EN_CONTRA_DE_LA_ENTIDAD                             | COSTAS A FAVOR O EN CONTRA DE LA ENTIDAD                             | object         |
| 131 | LAS_COSTAS_LAS_DEBE_PAGAR_LA_NACION?                                 | LAS COSTAS LAS DEBE PAGAR LA NACIÓN?                                 | object         |
| 133 | tipo_arbitramento                                                    | nan                                                                  | object         |
| 134 | RESULT_TER                                                           | nan                                                                  | object         |
| 135 | RESULT_FT                                                            | nan                                                                  | datetime64[ns] |
| 136 | RESULT_FA                                                            | nan                                                                  | datetime64[ns] |
| 137 | nombre_ua                                                            | nan                                                                  | object         |
| 138 | ID_sector_eKogui                                                     | nan                                                                  | object         |
| 139 | nombre_ua_Sector                                                     | nan                                                                  | object         |



# Tabla REPORTE_DOCUMENTOS_LAUDOS

Permite al usuario tener la relación de los diferentes documentos de cada uno de los laudos arbitrales que se han proferido, en este se guarda la relación con el campo ID_ARB. Los siguientes son los campos que incluye este reporte:

| Caolumna | Descripción | Tipo |
| -- | -- | -- |
| ID_ARB | Identificador del Arbitramento | Object |
| orfeo_no. | Identificador de SGDA | Object |
| URL | Link para el documento | Object |