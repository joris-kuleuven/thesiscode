import json
import os
from urllib.parse import urlparse

# Open the input file and load the data
with open('typescript_cve.json', 'r') as f:
    data = json.load(f)

# Prepare the output data
output_data = []
for item in data:
    new_item = {
        'app': item['app'],
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
            'versionEndIncluding': cpeMatch.get('versionEndIncluding'),
            'versionEndExcluding': cpeMatch.get('versionEndExcluding'),
            'versionStartExcluding': cpeMatch.get('versionStartExcluding')
        })

    # Extract the common part of the URLs in the references field
    if 'references' in item:
        commit_urls = [url for url in item['references'] if 'commit' in url]
        if commit_urls:
            new_item['commit_id'] = commit_urls

    common_path = os.path.commonprefix(item['references'])
    parsed_url = urlparse(common_path)
    base_path = '/'.join(parsed_url.path.split('/')[:3])
    repo_url = f"{parsed_url.scheme}://{parsed_url.netloc}{base_path}"
    new_item['repo_url'] = repo_url

    # Extract the weakness description value
    if 'original_vuln' in item and 'cve' in item['original_vuln'] and 'weaknesses' in item['original_vuln']['cve']:
        weaknesses = item['original_vuln']['cve']['weaknesses']
        weakness_descriptions = []
        for weakness in weaknesses:
            if 'description' in weakness:
                descriptions = weakness['description']
                for description in descriptions:
                    if 'value' in description:
                        weakness_descriptions.append(description['value'])
        if weakness_descriptions:
            new_item['cwe_id'] = weakness_descriptions


    output_data.append(new_item)

# Write the output data to the output file
with open('typescript_bv.json', 'w') as f:
    json.dump(output_data, f, indent=4)