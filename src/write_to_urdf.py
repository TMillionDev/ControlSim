def write(l, w, wgt):
    length = str(l)
    length2 = str(float(l) + 0.5)
    width = str(w)
    weight = str(wgt)

    urdf_template = """
<robot name="Arm">
    <link name="base">
        <visual>
            <origin xyz="0 0 -3.25" rpy="0 1.57 0"/>
            <geometry>
                <box size="0.5 5 """ + str(int(width) + 5) + """\"/>
            </geometry>
        <material name="Cyan1">
                <color rgba="0 0.8 0.8 1.0"/>
            </material>
        </visual>
        <collision>
            <origin xyz="0 0 -3.25" rpy="0 1.57 0"/>
            <geometry>
                <box size="0.5 5 5"/>
            </geometry>
        </collision>
        <inertial>
            <mass value="0"/>
            <origin xyz="0 0 -3.25" rpy="0 1.57 0"/>
            <inertia ixx="0.0" ixy="0.0" ixz="0.0" iyy="0.0" iyz="0.0" izz="0.0"/>
         </inertial>
    </link>
    <link name="tube">
        <visual>
            <origin xyz="0 0 -1" rpy="0 0 0"/>
            <geometry>
                <box size=\"""" + width + """ 0.5 """ + length + """\"/>
            </geometry>
            <material name="Blue1">
                <color rgba="0 0 1.0 1.0"/>
            </material>
        </visual>
        <collision>
            <origin xyz="0 0 -1" rpy="0 0 0"/>
            <geometry>
                <box size=\"""" + width + """ 0.5 """ + length + """\"/>
            </geometry>
        </collision>
        <inertial>
            <mass value=\"""" + weight + """\"/>
            <origin xyz="0 0 -1" rpy="0 0 0"/>
            <inertia ixx="5.4167" ixy="0.0" ixz="0.0" iyy="5.4167" iyz="0.0" izz="0.4167"/>
        </inertial>
    </link>
    <link name="motor">
        <visual>
            <origin xyz="-0.5 0 -0.25" rpy="0 1.57 0"/>
            <geometry>
                <cylinder radius="0.25" length="1"/>
            </geometry>
            <material name="Cyan1">
                <color rgba="0 0.9 0.9 1.0"/>
            </material>
        </visual>
        <collision>
            <origin xyz="-0.5 0 -0.25" rpy="0 1.57 0"/>
            <geometry>
                <cylinder radius="0.25" length="1"/>
            </geometry>
        </collision>
        <inertial>
            <mass value="2.0"/>
            <origin xyz="-0.5 0 -0.25" rpy="0 1.57 0"/>
            <inertia ixx="0.0" ixy="0.0" ixz="0.0" iyy="0.0" iyz="0.0" izz="0.0"/>
        </inertial>
    </link>
    <link name="axle">
        <visual>
            <origin xyz="0 0 0.25" rpy="0 1.57 0"/>
            <geometry>
                <cylinder radius="0.25" length="1"/>
            </geometry>
            <material name="Cyan1">
                <color rgba="0 0.9 0.9 1.0"/>
            </material>
        </visual>
        <collision>
            <origin xyz="0 0 0.25" rpy="0 1.57 0"/>
            <geometry>
                <cylinder radius="0.25" length="1"/>
            </geometry>
        </collision>
        <inertial>
            <mass value="2.0"/>
            <origin xyz="0 0 0.25" rpy="0 1.57 0"/>
            <inertia ixx="0.0" ixy="0.0" ixz="0.0" iyy="0.0" iyz="0.0" izz="0.0"/>
        </inertial>
    </link>
    <link name="support2">
        <visual>
            <origin xyz="1 0 -1" rpy="0 0 0"/>
            <geometry>
               <box size="1 1 """ + length2 + """\"/>
            </geometry>
        </visual>
        <collision>
            <origin xyz="1 0 -1" rpy="0 0 0"/>
            <geometry>
                <box size="1 1 """ + length2 + """\"/>
            </geometry>
        </collision>
        <inertial>
            <mass value="100.0"/>
            <origin xyz="1 0 -1" rpy="0 0 0"/>
            <inertia ixx="0.0" ixy="0.0" ixz="0.0" iyy="0.0" iyz="0.0" izz="0.0"/>
        </inertial>
    </link>
    <link name="support1">
        <visual>
            <origin xyz="0 0 1.5" rpy="0 0 0"/>
            <geometry>
                <box size="1 1 """ + length2 + """\"/>
            </geometry>
        </visual>
        <collision>
            <origin xyz="0 0 1.5" rpy="0 0 0"/>
            <geometry>
                <box size="1 1 """ + length2 + """\"/>
            </geometry>
        </collision>
        <inertial>
            <mass value="100.0"/>
            <origin xyz="0 0 1.5" rpy="0 0 0"/>
            <inertia ixx="0.0" ixy="0.0" ixz="0.0" iyy="0.0" iyz="0.0" izz="0.0"/>
        </inertial>
    </link>
    <joint name="support2_to_base" type="fixed">
        <parent link="base"/>
        <child link="support2"/>
        <origin xyz="1 0 """ + str(-2.0 + float(length)/2) + """\" rpy="0 0 0"/>
    </joint>
    <joint name="support1_to_base" type="fixed">
        <parent link="base"/>
        <child link="support1"/>
        <origin xyz="-1.5 0 """ + str(-4.5 + float(length)/2) + """\" rpy="0 0 0"/>
    </joint>
    <joint name="axle_to_support2" type="fixed">
        <parent link="support2"/>
        <child link="axle"/>
        <origin xyz="0 0 0" rpy="0 0 0"/>
    </joint>
    <joint name="motor_to_support1" type="fixed">
        <parent link="support1"/>
        <child link="motor"/>
        <origin xyz="1.5 0 3" rpy="0 0 0"/>
    </joint>
    <joint name="motor_to_tube" type="revolute">
        <parent link="motor"/>
        <child link="tube"/>
        <origin xyz="0.25 0 -0.25" rpy="0 0 0"/> 
        <axis xyz="1 0 0"/> 
        <limit effort="1" velocity="1.0" lower="0" upper="6.2832"/>
        <dynamics damping="0.01" friction="0.01"/>
    </joint>
</robot> """

    with open('arm.urdf', 'w') as f:
        f.write(urdf_template)

    print("URDF generated")

write(3, 2, 11)