#!/usr/bin/env python3
"""
更新 service-worker.js 中的 revision 哈希
"""

import hashlib
import re
import os

def calculate_md5(filepath):
    """计算文件的 MD5 哈希"""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except:
        return None

def update_service_worker():
    project_dir = '/Users/jadenli/CodeSpace/intfocus.archived.jaden.tech'
    sw_path = os.path.join(project_dir, 'service-worker.js')
    
    # 读取 service-worker.js
    with open(sw_path, 'r') as f:
        content = f.read()
    
    # 找到所有 {url:"...", revision:"..."} 模式
    pattern = r'\{url:"([^"]+)",revision:"([^"]+)"\}'
    
    updated_count = 0
    
    def replace_revision(match):
        nonlocal updated_count
        url = match.group(1)
        old_revision = match.group(2)
        
        # 构建文件路径
        filepath = os.path.join(project_dir, url)
        
        # 计算新的 MD5
        new_revision = calculate_md5(filepath)
        
        if new_revision:
            if new_revision != old_revision:
                updated_count += 1
                print(f"  更新: {url[:50]:50s} {old_revision[:8]}... -> {new_revision[:8]}...")
            return f'{{url:"{url}",revision:"{new_revision}"}}'
        else:
            print(f"  跳过: {url[:50]:50s} (文件不存在)")
            return match.group(0)
    
    # 替换所有 revision
    new_content = re.sub(pattern, replace_revision, content)
    
    # 写入更新后的文件
    with open(sw_path, 'w') as f:
        f.write(new_content)
    
    print(f"\n✅ service-worker.js 已更新")
    print(f"   更新了 {updated_count} 个文件的 revision")

if __name__ == '__main__':
    update_service_worker()
