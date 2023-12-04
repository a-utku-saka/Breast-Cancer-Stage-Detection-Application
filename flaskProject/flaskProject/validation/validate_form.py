def validate_form_data(data):
    result = list()
    
    # for chemotherapy values
    chemotherapy_value = 'chemotherapy' in data and data['chemotherapy']
    result.append(1 if chemotherapy_value else 0)
    
    # for neoplasm histologic grade
    result.append(float(data['nhg']))
    
    # for hormone therapy value
    hormone_therapy = 'hormone_therapy' in data and data['hormone_therapy']
    result.append(1.0 if hormone_therapy else 0.0)
    
    # positive lymph nodes
    lnp = float(data['positive_lymph_nodes'])
    result.append(lnp)
    
    # for nottingham prognostic index
    nottingham_index = float(data['nottingham-index'])
    result.append(nottingham_index)
    
    # for radiotherapy values
    radiotherapy_value = 'radiotherapy' in data and data['radiotherapy']
    result.append(1.0 if radiotherapy_value else 0.0)
    
    # for tumor_size
    tumor_size = float(data['tumor_size'])
    result.append(tumor_size)
    
    # for breast surgery type
    breast_surgery = data['breast-surgery']
    if breast_surgery == 'mastectomy':
        breast_surgery = 1.0
    elif breast_surgery == 'breast-conserving':
        breast_surgery = 0.0
    result.append(breast_surgery)
    
    # for cancer type
    cancer_type = data['cancer-type']
    if cancer_type == 'ductal':
        lobular, mixed = 0.0, 0.0
    elif cancer_type == 'mixed':
        lobular = 0.0
        mixed = 1.0
    else:
        lobular = 1.0
        mixed = 0.0
    result.append(lobular)
    result.append(mixed)

    # for cellularity
    cellularity_value = data['cellularity']
    if cellularity_value == 'low':
        low, moderate = 1.0, 0.0
    elif cellularity_value == 'moderate':
        low, moderate = 0.0, 1.0
    else:
        low, moderate = 0.0, 0.0
    result.append(low)
    result.append(moderate)

    # for pam50
    pam_50 = data['pam50']
    if pam_50 == 'her2':
        her_2, lum_a, lum_b, normal, low = 1.0, 0, 0, 0, 0
    elif pam_50 == 'lumA':
        her_2, lum_a, lum_b, normal, low = 0, 1.0, 0, 0, 0
    elif pam_50 == 'lumB':
        her_2, lum_a, lum_b, normal, low = 0, 0, 1.0, 0, 0
    elif pam_50 == 'normal':
        her_2, lum_a, lum_b, normal, low = 0, 0, 0, 1.0, 0
    elif pam_50 == 'low_pam50':
        her_2, lum_a, lum_b, normal, low = 0, 0, 0, 0, 1.0
    else:
        her_2, lum_a, lum_b, normal, low = 0, 0, 0, 0, 0.0
    result.append(her_2)
    result.append(lum_a)
    result.append(lum_b)
    result.append(normal)
    result.append(low)

    # for er status
    er_status = data['er_status']
    if er_status == 'positive':
        positive = 1.0
    else:
        positive = 0.0
    result.append(positive)

    # for her2 status
    her_2_status = data['her2_status']
    if her_2_status == 'positive':
        her_2_positive = 1.0
    else:
        her_2_positive = 0.0
    result.append(her_2_positive)

    # for tumor other histologic subtype
    tumor_other = data['tumor_other']
    if tumor_other == 'lobular':
        lobular, mixed = 1.0, 0
    elif tumor_other == 'mixed_tumor':
        lobular, mixed = 0, 1.0
    else:
        lobular, mixed = 0.0, 0
    result.append(lobular)
    result.append(mixed)

    # for menopausal state
    menopausal_state = data['menopausal_state']
    if menopausal_state == 'pre':
        pre = 1.0
    else:
        pre = 0.0
    result.append(pre)

    # for pr_status
    pr_status = data['pr_status']
    if pr_status == 'pr_positive':
        pr_positive = 1.0
    else:
        pr_positive = 0.0
    result.append(pr_positive)

    # for 3 gene classifier subtype
    gene = data['3_gene']
    if gene == 'low_prolif':
        low_prolif, er_, her_2_positive = 1.0, 0, 0
    elif gene == 'er_':
        low_prolif, er_, her_2_positive = 0, 1.0, 0
    elif gene == 'her2+':
        low_prolif, er_, her_2_positive = 0, 0, 1.0
    else:
        low_prolif, er_, her_2_positive = 0, 0.0, 0
    result.append(low_prolif)
    result.append(er_)
    result.append(her_2_positive)

    age = data['age']

    if age == '20-40':
        age_40_60, age_60_80, age_80_100 = 0.0, 0, 0
    elif age == '40-60':
        age_40_60, age_60_80, age_80_100 = 1.0, 0, 0
    elif age == '60-80':
        age_40_60, age_60_80, age_80_100 = 0.0, 1.0, 0
    else:
        age_40_60, age_60_80, age_80_100 = 0.0, 0, 1.0
    result.append(age_40_60)
    result.append(age_60_80)
    result.append(age_80_100)
    return result
