import json
import os

# Open the input file and load the data
with open('typescript_cve.json', 'r') as f:
    data = json.load(f)

# Prepare the output data
output_data = []
for item in data:
    new_item = {
        'cve_id': item['cve_id'],
        'published': item['original_vuln']['cve']['published'],
        'lastModified': item['original_vuln']['cve']['lastModified'],
    }

    # Iterate over each object in the metrics field
    for metric_name, metric_value in item['original_vuln']['cve']['metrics'].items():
        # Check if the object name starts with cvssMetric
        if metric_name.startswith('cvssMetric'):
            cvssData = metric_value[0]['cvssData']
            new_item.update({
                'accessComplexity': cvssData.get('accessComplexity') or cvssData.get('attackComplexity'),
                'authentication': cvssData.get('authentication') or cvssData.get('privilegesRequired'),
                'availabilityImpact': cvssData.get('availabilityImpact'),
                'confidentialityImpact': cvssData.get('confidentialityImpact'),
                'baseScore': cvssData.get('baseScore'),
                'integrityImpact': cvssData.get('integrityImpact'),
            })

    # Check if configurations are present
    if 'configurations' in item['original_vuln']['cve']:
        cpeMatch = item['original_vuln']['cve']['configurations'][0]['nodes'][0]['cpeMatch'][0]
        new_item.update({
            'versionStartIncluding': cpeMatch.get('versionStartIncluding'),
            'versionEndExcluding': cpeMatch.get('versionEndExcluding'),
        })

    # Extract the common part of the URLs in the references field
    if 'references' in item:
        common_path = os.path.commonprefix(item['references'])
        new_item['references'] = common_path

    output_data.append(new_item)

# Write the output data to the output file
with open('typescript_bv.json', 'w') as f:
    json.dump(output_data, f, indent=4)