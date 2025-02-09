#Copy https://woow3d.com/ 
#2025 February 10, 01:37 AM

import os
import bpy

# تحديد مسار المجلدات
directory_path = "E:\Blender\Blender Asset"  # عدّل المسار حسب الحاجة



# التحقق من صحة المسار
if not os.path.exists(directory_path):
    print("❌ المسار غير موجود، تحقق من إدخال المسار الصحيح.")
else:
    # تمرير التفضيلات للوصول إلى مكتبات الأصول
    prefs = bpy.context.preferences.filepaths

    # إضافة جميع المجلدات كمكتبات أصول
    for folder_name in os.listdir(directory_path):
        folder_path = os.path.join(directory_path, folder_name)
        if os.path.isdir(folder_path):  # التأكد من أنه مجلد
            if folder_name not in prefs.asset_libraries:
                prefs.asset_libraries.new(name=folder_name, directory=folder_path)
                print(f"✅ تمت إضافة مكتبة الأصول '{folder_name}' في: {folder_path}")
            else:
                print(f"⚠️ مكتبة الأصول '{folder_name}' موجودة بالفعل.")

    # حفظ التفضيلات بعد التعديل
    bpy.ops.wm.save_userpref()
    print("💾 تم حفظ إعدادات المكتبات بنجاح.")
