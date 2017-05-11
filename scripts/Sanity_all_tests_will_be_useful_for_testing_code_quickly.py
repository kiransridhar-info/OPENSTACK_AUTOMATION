import subprocess
import os
from json import loads
from json import dumps
from pprint import pprint as pp
import ast
import time
import sys
import re

sys.path.insert(0,"../lib")
from os_objects import *

# ACTION : YOU NEED TO GET THESE DATA FROM JSON , USE A FUNCTION CALL AS PART OF PRESETUP
o_chdir = os.chdir("/opt/stack/devstack")
size_vol = 65
type_vol = 'VMAX_SILVER'
image = 'cirros-0.3.4-x86_64-uec' #Keep a function here to get the value automatically.
flavor = 'm1.tiny'
no_attach = []
replication_status = None
volume_available_string = 'available'
server_available_string = 'ACTIVE'
bootable_string = 'true'
non_rep_vol_type = 'VMAX_SILVER'


number_of_volumes_to_create = 3
extension_factor_input = 30
number_of_snapshots_per_volume = 2
volumes_name_prefix = str(sys.argv[1])

server_name =  'qe' + '_server_' + str(time.time())# ACTION : Should be combination of testname, qe, server, timestamp of creation

# Object Instantiation for volumes
os_objects_handle_volume = VolumeOperations()

# MULTIPLE NON BOOTABLE VOLUME CREATION
# non_bootable_volume_list = os_objects_handle_volume.volumes_create(volumes_name_prefix = volumes_name_prefix,
#                                                                      number_of_volumes=number_of_volumes_to_create)

non_bootable_volume_list =  [{'status': 'available', 'migration_status': None, 'attachments': [], 'availability_zone': 'nova', 'os-vol-host-attr:host': 'dldv0030@VMAX_BRONZE#Diamond+SRP_1+000196801125', 'encrypted': False, 'updated_at': '2017-05-10T08:24:04.000000', 'source_volid': None, 'consistencygroup_id': None, 'replication_status': 'disabled', 'snapshot_id': None, 'id': '96e8a1c5-d3a0-4f9f-875e-c55104920123', 'os-vol-mig-status-attr:name_id': None, 'size': 20, 'user_id': 'bb80baecc5bc43f3aaa69245d998158c', 'name': 'QE_10_900', 'bootable': 'false', 'description': None, 'multiattach': False, 'properties': '', 'os-vol-tenant-attr:tenant_id': 'aa6c32d34a6143acb3f116c754dde19f', 'type': 'VMAX_BRONZE', 'created_at': '2017-05-10T08:17:08.000000', 'os-vol-mig-status-attr:migstat': None}, {'status': 'available', 'migration_status': None, 'attachments': [], 'availability_zone': 'nova', 'os-vol-host-attr:host': 'dldv0030@VMAX_DIAMOND#Diamond+SRP_1+000196801125', 'encrypted': False, 'updated_at': '2017-05-10T08:18:53.000000', 'source_volid': None, 'consistencygroup_id': None, 'replication_status': 'disabled', 'snapshot_id': None, 'id': '0936cdb5-c4bf-4f9b-8555-873c8810031a', 'os-vol-mig-status-attr:name_id': None, 'size': 23, 'user_id': 'bb80baecc5bc43f3aaa69245d998158c', 'name': 'QE_10_901', 'bootable': 'false', 'description': None, 'multiattach': False, 'properties': '', 'os-vol-tenant-attr:tenant_id': 'aa6c32d34a6143acb3f116c754dde19f', 'type': 'VMAX_DIAMOND', 'created_at': '2017-05-10T08:17:17.000000', 'os-vol-mig-status-attr:migstat': None}, {'status': 'available', 'migration_status': None, 'attachments': [], 'availability_zone': 'nova', 'os-vol-host-attr:host': 'dldv0030@VMAX_BRONZE#Diamond+SRP_1+000196801125', 'encrypted': False, 'updated_at': '2017-05-10T08:24:34.000000', 'source_volid': None, 'consistencygroup_id': None, 'replication_status': 'disabled', 'snapshot_id': None, 'id': '2fa0117b-674c-44cb-96df-f0368a9c92cf', 'os-vol-mig-status-attr:name_id': None, 'size': 23, 'user_id': 'bb80baecc5bc43f3aaa69245d998158c', 'name': 'QE_10_902', 'bootable': 'false', 'description': None, 'multiattach': False, 'properties': '', 'os-vol-tenant-attr:tenant_id': 'aa6c32d34a6143acb3f116c754dde19f', 'type': 'VMAX_BRONZE', 'created_at': '2017-05-10T08:17:27.000000', 'os-vol-mig-status-attr:migstat': None}]


# non_bootable_volume_list = [{'status': 'available', 'migration_status': None, 'attachments': [], 'availability_zone': 'nova', 'os-vol-host-attr:host': 'dldv0030@VMAX_BRONZE#Diamond+SRP_1+000196801125', 'encrypted': False, 'updated_at': '2017-05-10T07:25:38.000000', 'source_volid': None, 'consistencygroup_id': None, 'replication_status': 'disabled', 'snapshot_id': None, 'id': 'e86361fa-9428-4170-8da3-5b890fdcb518', 'os-vol-mig-status-attr:name_id': None, 'size': 22, 'user_id': 'bb80baecc5bc43f3aaa69245d998158c', 'name': 'QE_10_70', 'bootable': 'false', 'description': None, 'multiattach': False, 'properties': '', 'os-vol-tenant-attr:tenant_id': 'aa6c32d34a6143acb3f116c754dde19f', 'type': 'VMAX_BRONZE', 'created_at': '2017-05-10T07:25:15.000000', 'os-vol-mig-status-attr:migstat': None}, {'status': 'available', 'migration_status': None, 'attachments': [], 'availability_zone': 'nova', 'os-vol-host-attr:host': 'dldv0030@VMAX_DIAMOND#Diamond+SRP_1+000196801125', 'encrypted': False, 'updated_at': '2017-05-10T07:25:58.000000', 'source_volid': None, 'consistencygroup_id': None, 'replication_status': 'disabled', 'snapshot_id': None, 'id': 'e95d35c4-0914-4be7-a35a-407a914f9628', 'os-vol-mig-status-attr:name_id': None, 'size': 22, 'user_id': 'bb80baecc5bc43f3aaa69245d998158c', 'name': 'QE_10_71', 'bootable': 'false', 'description': None, 'multiattach': False, 'properties': '', 'os-vol-tenant-attr:tenant_id': 'aa6c32d34a6143acb3f116c754dde19f', 'type': 'VMAX_DIAMOND', 'created_at': '2017-05-10T07:25:25.000000', 'os-vol-mig-status-attr:migstat': None}, {'status': 'available', 'migration_status': None, 'attachments': [], 'availability_zone': 'nova', 'os-vol-host-attr:host': 'dldv0030@VMAX_BRONZE#Diamond+SRP_1+000196801125', 'encrypted': False, 'updated_at': '2017-05-10T07:26:28.000000', 'source_volid': None, 'consistencygroup_id': None, 'replication_status': 'disabled', 'snapshot_id': None, 'id': '199690eb-3926-4a6d-b41f-d5cd86639004', 'os-vol-mig-status-attr:name_id': None, 'size': 25, 'user_id': 'bb80baecc5bc43f3aaa69245d998158c', 'name': 'QE_10_72', 'bootable': 'false', 'description': None, 'multiattach': False, 'properties': '', 'os-vol-tenant-attr:tenant_id': 'aa6c32d34a6143acb3f116c754dde19f', 'type': 'VMAX_BRONZE', 'created_at': '2017-05-10T07:25:34.000000', 'os-vol-mig-status-attr:migstat': None}]

# #
# # MULTIPLE BOOTABLE VOLUME CREATION
# bootable_volume_list = os_objects_handle_volume.volumes_create(bootable_factor = 'bootable',
#                                                                volumes_name_prefix = 'BNG123',
#                                                                number_of_volumes=number_of_volumes_to_create)
# # EXTEND VOLUME
# non_bootable_volume_list = os_objects_handle_volume.volumes_extend(non_bootable_volume_list,
#                                                      extension_factor = extension_factor_input)
# bootable_volume_list = os_objects_handle_volume.volumes_extend(bootable_volume_list,
#                                                                   extension_factor = extension_factor_input)

# Object Instantiation for snapshots
os_objects_handle_snapshots = SnapshotOperations()

# SNAPSHOT CREATION OF UNATTACHED VOLUMES
print "\nMAIN SCRIPT : SNAPSHOT CREATE..."
(input_volume_list, created_snapshot_list, volume_snapshot_mapping) = os_objects_handle_snapshots.snapshots_create(
                                                                                   snapshot_prefix = "TF_Snap_",
                                                                                   volume_list = non_bootable_volume_list,
                                                                                   number_of_snapshots_per_volume=
                                                                                   number_of_snapshots_per_volume)
#
# print "\ncreated_snapshot_list %s" %created_snapshot_list
# print "\ninput_volume_list %s" %input_volume_list
# print "\ndictionary %s" %volume_snapshot_mapping

# created_snapshot_list = [[{'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9000', 'created_at': '2017-05-10T08:24:54.000000', 'updated_at': '2017-05-10T08:58:56.000000', 'id': 'b7465e04-70ae-497d-8ea9-8e93adf6920e', 'volume_id': '96e8a1c5-d3a0-4f9f-875e-c55104920123', 'size': 20, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_900_0'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9001', 'created_at': '2017-05-10T08:24:57.000000', 'updated_at': '2017-05-10T09:00:18.000000', 'id': '265d4f0a-0268-4274-8628-5a7086ff489d', 'volume_id': '96e8a1c5-d3a0-4f9f-875e-c55104920123', 'size': 20, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_900_1'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9002', 'created_at': '2017-05-10T08:24:59.000000', 'updated_at': '2017-05-10T09:01:07.000000', 'id': 'f1676172-4029-41d8-8486-5829f359fb6d', 'volume_id': '96e8a1c5-d3a0-4f9f-875e-c55104920123', 'size': 20, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_900_2'}], [{'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9010', 'created_at': '2017-05-10T08:25:02.000000', 'updated_at': '2017-05-10T08:39:47.000000', 'id': '32cbf38a-e82e-4b9e-9853-b7cea810aee6', 'volume_id': '0936cdb5-c4bf-4f9b-8555-873c8810031a', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_901_0'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9011', 'created_at': '2017-05-10T08:25:05.000000', 'updated_at': '2017-05-10T08:40:37.000000', 'id': '358a0c74-8806-4c93-983d-eb8742288b23', 'volume_id': '0936cdb5-c4bf-4f9b-8555-873c8810031a', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_901_1'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9012', 'created_at': '2017-05-10T08:25:07.000000', 'updated_at': '2017-05-10T08:41:57.000000', 'id': 'bd7fb71c-18fc-4bf7-b6e2-2403e4c75fb3', 'volume_id': '0936cdb5-c4bf-4f9b-8555-873c8810031a', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_901_2'}], [{'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9020', 'created_at': '2017-05-10T08:25:10.000000', 'updated_at': '2017-05-10T09:05:07.000000', 'id': '72ba6d12-9a52-49f4-a611-235ce00cf160', 'volume_id': '2fa0117b-674c-44cb-96df-f0368a9c92cf', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_902_0'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9021', 'created_at': '2017-05-10T08:25:13.000000', 'updated_at': '2017-05-10T09:06:57.000000', 'id': 'f296c4cf-5995-4264-b019-14ccb06903a1', 'volume_id': '2fa0117b-674c-44cb-96df-f0368a9c92cf', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_902_1'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9022', 'created_at': '2017-05-10T08:25:15.000000', 'updated_at': '2017-05-10T09:07:37.000000', 'id': 'd71419ab-8f9f-4370-a184-95083d030fc5', 'volume_id': '2fa0117b-674c-44cb-96df-f0368a9c92cf', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_902_2'}]]
# # non_bootable_volume_list = [{'status': 'available', 'migration_status': 'None', 'attachments': [], 'availability_zone': 'nova', 'os-vol-host-attr:host': 'dldv0030@VMAX_BRONZE#Diamond+SRP_1+000196801125', 'encrypted': 'False', 'updated_at': '2017-05-10T07:25:38.000000', 'source_volid': 'None', 'consistencygroup_id': 'None', 'replication_status': 'disabled', 'snapshot_id': 'None', 'id': 'e86361fa-9428-4170-8da3-5b890fdcb518', 'os-vol-mig-status-attr:name_id': 'None', 'size': 22, 'user_id': 'bb80baecc5bc43f3aaa69245d998158c', 'name': 'QE_10_70', 'bootable': 'false', 'description': 'None', 'multiattach': 'False', 'properties': '', 'os-vol-tenant-attr:tenant_id': 'aa6c32d34a6143acb3f116c754dde19f', 'type': 'VMAX_BRONZE', 'created_at': '2017-05-10T07:25:15.000000', 'os-vol-mig-status-attr:migstat': 'None'}, {'status': 'available', 'migration_status': 'None', 'attachments': [], 'availability_zone': 'nova', 'os-vol-host-attr:host': 'dldv0030@VMAX_DIAMOND#Diamond+SRP_1+000196801125', 'encrypted': 'False', 'updated_at': '2017-05-10T07:25:58.000000', 'source_volid': 'None', 'consistencygroup_id': 'None', 'replication_status': 'disabled', 'snapshot_id': 'None', 'id': 'e95d35c4-0914-4be7-a35a-407a914f9628', 'os-vol-mig-status-attr:name_id': 'None', 'size': 22, 'user_id': 'bb80baecc5bc43f3aaa69245d998158c', 'name': 'QE_10_71', 'bootable': 'false', 'description': 'None', 'multiattach': 'False', 'properties': '', 'os-vol-tenant-attr:tenant_id': 'aa6c32d34a6143acb3f116c754dde19f', 'type': 'VMAX_DIAMOND', 'created_at': '2017-05-10T07:25:25.000000', 'os-vol-mig-status-attr:migstat': 'None'}, {'status': 'available', 'migration_status': 'None', 'attachments': [], 'availability_zone': 'nova', 'os-vol-host-attr:host': 'dldv0030@VMAX_BRONZE#Diamond+SRP_1+000196801125', 'encrypted': 'False', 'updated_at': '2017-05-10T07:26:28.000000', 'source_volid': 'None', 'consistencygroup_id': 'None', 'replication_status': 'disabled', 'snapshot_id': 'None', 'id': '199690eb-3926-4a6d-b41f-d5cd86639004', 'os-vol-mig-status-attr:name_id': None, 'size': 25, 'user_id': 'bb80baecc5bc43f3aaa69245d998158c', 'name': 'QE_10_72', 'bootable': 'false', 'description': 'None', 'multiattach': 'False', 'properties': '', 'os-vol-tenant-attr:tenant_id': 'aa6c32d34a6143acb3f116c754dde19f', 'type': 'VMAX_BRONZE', 'created_at': '2017-05-10T07:25:34.000000', 'os-vol-mig-status-attr:migstat': 'None'}]
# volume_snapshot_mapping = {'QE_10_902': [{'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9020', 'created_at': '2017-05-10T08:25:10.000000', 'updated_at': '2017-05-10T09:05:07.000000', 'id': '72ba6d12-9a52-49f4-a611-235ce00cf160', 'volume_id': '2fa0117b-674c-44cb-96df-f0368a9c92cf', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_902_0'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9021', 'created_at': '2017-05-10T08:25:13.000000', 'updated_at': '2017-05-10T09:06:57.000000', 'id': 'f296c4cf-5995-4264-b019-14ccb06903a1', 'volume_id': '2fa0117b-674c-44cb-96df-f0368a9c92cf', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_902_1'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9022', 'created_at': '2017-05-10T08:25:15.000000', 'updated_at': '2017-05-10T09:07:37.000000', 'id': 'd71419ab-8f9f-4370-a184-95083d030fc5', 'volume_id': '2fa0117b-674c-44cb-96df-f0368a9c92cf', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_902_2'}], 'QE_10_901': [{'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9010', 'created_at': '2017-05-10T08:25:02.000000', 'updated_at': '2017-05-10T08:39:47.000000', 'id': '32cbf38a-e82e-4b9e-9853-b7cea810aee6', 'volume_id': '0936cdb5-c4bf-4f9b-8555-873c8810031a', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_901_0'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9011', 'created_at': '2017-05-10T08:25:05.000000', 'updated_at': '2017-05-10T08:40:37.000000', 'id': '358a0c74-8806-4c93-983d-eb8742288b23', 'volume_id': '0936cdb5-c4bf-4f9b-8555-873c8810031a', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_901_1'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9012', 'created_at': '2017-05-10T08:25:07.000000', 'updated_at': '2017-05-10T08:41:57.000000', 'id': 'bd7fb71c-18fc-4bf7-b6e2-2403e4c75fb3', 'volume_id': '0936cdb5-c4bf-4f9b-8555-873c8810031a', 'size': 23, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_901_2'}], 'QE_10_900': [{'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9000', 'created_at': '2017-05-10T08:24:54.000000', 'updated_at': '2017-05-10T08:58:56.000000', 'id': 'b7465e04-70ae-497d-8ea9-8e93adf6920e', 'volume_id': '96e8a1c5-d3a0-4f9f-875e-c55104920123', 'size': 20, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_900_0'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9001', 'created_at': '2017-05-10T08:24:57.000000', 'updated_at': '2017-05-10T09:00:18.000000', 'id': '265d4f0a-0268-4274-8628-5a7086ff489d', 'volume_id': '96e8a1c5-d3a0-4f9f-875e-c55104920123', 'size': 20, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_900_1'}, {'status': 'available', 'properties': '', 'os-extended-snapshot-attributes:progress': '100%', 'description': 'THIS IS SNAPSHOT snap_QE_10_9002', 'created_at': '2017-05-10T08:24:59.000000', 'updated_at': '2017-05-10T09:01:07.000000', 'id': 'f1676172-4029-41d8-8486-5829f359fb6d', 'volume_id': '96e8a1c5-d3a0-4f9f-875e-c55104920123', 'size': 20, 'os-extended-snapshot-attributes:project_id': 'aa6c32d34a6143acb3f116c754dde19f', 'name': 'snap_QE_10_900_2'}]}

# CREATE VOLUMES FROM SOURCE=SNAPSHOT
print "\nMAIN SCRIPT : VOLUME CREATE FROM SNAPSHOT"
volume_cloned_from_snapshot_prefix = 'cloned_from_snapshot'
cloned_from_snapshot_list = os_objects_handle_volume.volumes_clone(type_of_source = "snapshot",
                                                                   input_volume_list = non_bootable_volume_list,
                                                                   created_snapshot_list = created_snapshot_list,
                                                                   dict_of_volname_snapshot = volume_snapshot_mapping,
                                                                   name_prefix_of_target =
                                                                   volume_cloned_from_snapshot_prefix,
                                                                   number_of_snapshots_per_volume=
                                                                   number_of_snapshots_per_volume)

# CREATE VOLUMES FROM SOURCE=NON BOOTABLE VOLUME
print "\nMAIN SCRIPT : VOLUME CREATE FROM NON BOOTABLE VOLUME"
volume_cloned_from_volume_prefix = 'cloned_from_bootable_'
cloned_from_non_bootable_volume_list = os_objects_handle_volume.volumes_clone(type_of_source = "volume",
                                                                              input_volume_list =
                                                                              non_bootable_volume_list,
                                                                              name_prefix_of_target =
                                                                              volume_cloned_from_volume_prefix)
#
# # CREATE VOLUMES FROM SOURCE=BOOTABLE VOLUME
# print "\nMAIN SCRIPT : VOLUME CREATE FROM BOOTABLE VOLUME"
# volume_cloned_from_volume_prefix = 'cloned_from_bootable_'
# cloned_from_bootable_volume_list = os_objects_handle_volume.volumes_clone("volume",
#                                                                                bootable_volume_list,
#                                                                                volume_cloned_from_volume_prefix)
# #
# # INSTANCE CREATION
# os_objects_handle_server = InstanceOperations(server_name,image,flavor)
# print "\nMAIN SCRIPT : INSTANCE CREATION..." , os_objects_handle_server.server_create()
#
# # ATTACH VOLUME
# print "\nMAIN SCRIPT : VOLUME ATTACH...",os_objects_handle_server.volume_attach(volume_name)
#
# # SNAPSHOT CREATION OF ATTACHED VOLUME
# print "\nMAIN SCRIPT : SNAPSHOT CREATE..."
# snapshot_name_1 = os_objects_handle_volume.volume_snapshot_create(volume_name, number_of_snapshots)
#
# # DETACH VOLUMES
# print "\nMAIN SCRIPT : DETACH VOLUME..."
# volume_detach = os_objects_handle_server.volume_detach(volume_name)
#
# # SNAPSHOT CREATION OF NORMAL VOLUME AFTER DETACH
# print "\nMAIN SCRIPT : SNAPSHOT CREATE..."
# snapshot_name_2 = os_objects_handle_volume.volume_snapshot_create(volume_name, number_of_snapshots)
#

#
# DELETE ALL SNAPSHOTS
print "\nMAIN SCRIPT : VOLUME SNAPSHOT DELETION"
snapshot_delete = os_objects_handle_snapshots.snapshots_delete(non_bootable_volume_list,
                                                               dict_of_volume_snapshot_association,
                                                               number_of_snapshot_per_volume=
                                                               number_of_snapshot_per_volume)

# DELETE ALL VOLUMES
print "\nMAIN SCRIPT : VOLUME DELETION"
volume_delete_non_bootable = os_objects_handle_volume.volumes_delete(non_bootable_volume_list)
volume_delete_bootable = os_objects_handle_volume.volumes_delete(bootable_volume_list)

