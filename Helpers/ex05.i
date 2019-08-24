[Mesh]
  file = trialmesh.inp
[]

[Variables]
  [./convected]
    order = FIRST
    family = LAGRANGE
  [../]
  [./diffused]
    order = FIRST
    family = LAGRANGE
  [../]
[]

[Kernels]
  [./mat_diff]
    type=ExampleCoefDiffusion
    variable = convected
    coef = .1
  [../]
  [./3922_diff]
    type = ExampleCoefDiffusion
    variable = convected
    coef = .1
    block = '3922_TRI3'
  [../]
  [./1_diff]
    type = ExampleCoefDiffusion
    variable = convected
    coef = .1
    block = '1_TRI3'
  [../]
  [./conv]
    type = ExampleConvection
    variable = convected
    velocity = '5 0 0'
  [../]
  #This is just here to compare with our output
  [./diff]
    type = Diffusion
    variable = diffused
  [../]
[]

[BCs]
  # convected=0 on all vertical sides except the right (x-max)
  [./left_convected]
    type = DirichletBC
    variable = convected
    boundary = 'NRightSide'
    value = 1
  [../]
  [./right_convected]
    type = DirichletBC
    variable = convected
    boundary = 'NLeftSide'
    value = 0
  [../]
  [./left_diffused]
    type = DirichletBC
    variable = diffused
    boundary = 'NLeftSide'
    value = 0
  [../]
  [./right_diffused]
    type = DirichletBC
    variable = diffused
    boundary = 'NRightSide'
    value = 1
  [../]
[]

[Executioner]
  type = Steady
  solve_type = 'PJFNK'
[]

[Outputs]
  execute_on = 'timestep_end'
  exodus = true
[]
