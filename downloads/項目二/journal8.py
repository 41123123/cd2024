# NX 1872
# Journal created by User on Fri Jun 14 19:59:42 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Assemblies
import NXOpen.Positioning
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   功能表：組立件(A)->元件位置(P)->移動元件(E)...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    componentPositioner1 = workPart.ComponentAssembly.Positioner
    
    componentPositioner1.ClearNetwork()
    
    arrangement1 = workPart.ComponentAssembly.Arrangements.FindObject("Arrangement 1")
    componentPositioner1.PrimaryArrangement = arrangement1
    
    componentPositioner1.BeginMoveComponent()
    
    allowInterpartPositioning1 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    unit2 = workPart.UnitCollection.FindObject("Degrees")
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network1 = componentPositioner1.EstablishNetwork()
    
    componentNetwork1 = network1
    componentNetwork1.MoveObjectsState = True
    
    componentNetwork1.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork1.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    expression9 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    componentNetwork1.RemoveAllConstraints()
    
    movableObjects1 = []
    componentNetwork1.SetMovingGroup(movableObjects1)
    
    componentNetwork1.Solve()
    
    theSession.SetUndoMarkName(markId1, "移動元件 對話方塊")
    
    componentNetwork1.MoveObjectsState = True
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component Update")
    
    # ----------------------------------------------
    #   功能表：組立件(A)->元件位置(P)->組立約束(N)...
    # ----------------------------------------------
    componentPositioner1.EndMoveComponent()
    
    componentPositioner1.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMarksUpToMark(markId2, None, False)
    
    theSession.UndoToMark(markId1, None)
    
    theSession.DeleteUndoMark(markId1, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "通過定位任務建立約束")
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    componentPositioner2 = workPart.ComponentAssembly.Positioner
    
    componentPositioner2.ClearNetwork()
    
    componentPositioner2.PrimaryArrangement = arrangement1
    
    componentPositioner2.BeginAssemblyConstraints()
    
    allowInterpartPositioning2 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression18 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression19 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network2 = componentPositioner2.EstablishNetwork()
    
    componentNetwork2 = network2
    componentNetwork2.MoveObjectsState = True
    
    componentNetwork2.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork2.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId4, "組立約束 對話方塊")
    
    componentNetwork2.MoveObjectsState = True
    
    componentNetwork2.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    component1 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 2 3")
    face1 = component1.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 150 {(0,-7.5,-5) EXTRUDE(1)}")
    line1 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = -0.20295974723160859
    rotMatrix1.Xy = 0.19766584036814419
    rotMatrix1.Xz = -0.95902844408038102
    rotMatrix1.Yx = -0.57480889470584762
    rotMatrix1.Yy = -0.81695198821602277
    rotMatrix1.Yz = -0.046735249190805711
    rotMatrix1.Zx = -0.79271815645330179
    rotMatrix1.Zy = 0.54177270557074064
    rotMatrix1.Zz = 0.2794284522517998
    translation1 = NXOpen.Point3d(-109.54184623072666, 105.76906749578255, -328.04721137732378)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.44685142009170709)
    
    scaleAboutPoint1 = NXOpen.Point3d(-52.105313503434679, 187.1054439441516, 0.0)
    viewCenter1 = NXOpen.Point3d(52.105313503434481, -187.1054439441512, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(-41.210566134534773, 146.84224714604306, 0.0)
    viewCenter2 = NXOpen.Point3d(41.210566134534446, -146.84224714604267, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(-32.589505173057475, 117.09484998226405, 0.0)
    viewCenter3 = NXOpen.Point3d(32.589505173057084, -117.09484998226367, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(-26.071604138445974, 93.675879985811292, 0.0)
    viewCenter4 = NXOpen.Point3d(26.071604138445664, -93.675879985810894, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(-20.857283310756781, 74.940703988649062, 0.0)
    viewCenter5 = NXOpen.Point3d(20.857283310756511, -74.940703988648679, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    objects1 = [NXOpen.TaggedObject.Null] * 1 
    objects1[0] = line1
    nErrs1 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
    
    scaleAboutPoint6 = NXOpen.Point3d(-24.446676252607919, 19.014081529806241, 0.0)
    viewCenter6 = NXOpen.Point3d(24.446676252607652, -19.014081529805878, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(-32.983610817010636, 21.342336411006979, 0.0)
    viewCenter7 = NXOpen.Point3d(32.983610817010366, -21.34233641100661, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(-44.564253585483094, 23.949496824851579, 0.0)
    viewCenter8 = NXOpen.Point3d(44.564253585482838, -23.949496824851192, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(-59.494794327558154, 27.663184623641815, 0.0)
    viewCenter9 = NXOpen.Point3d(59.494794327557898, -27.663184623641424, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(-90.000086960477972, -81.473762932642941, 0.0)
    viewCenter10 = NXOpen.Point3d(90.000086960477773, 81.473762932643353, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(-72.000069568382457, -68.210592222677789, 0.0)
    viewCenter11 = NXOpen.Point3d(72.000069568382187, 68.210592222678173, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-57.600055654705955, -56.387422904080246, 0.0)
    viewCenter12 = NXOpen.Point3d(57.600055654705749, 56.387422904080665, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(-45.837517973639684, -45.594991423514351, 0.0)
    viewCenter13 = NXOpen.Point3d(45.837517973639521, 45.594991423514699, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(-36.67001437891178, -37.05805685911163, 0.0)
    viewCenter14 = NXOpen.Point3d(36.670014378911581, 37.058056859111993, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint14, viewCenter14)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint1 = componentPositioner2.CreateConstraint(True)
    
    componentConstraint1 = constraint1
    componentConstraint1.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.InferAlign
    
    componentConstraint1.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    component2 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 2 1")
    face2 = component2.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 120 {(0,0,0) EXTRUDE(1)}")
    constraintReference1 = componentConstraint1.CreateConstraintReference(component2, face2, False, False, False)
    
    helpPoint1 = NXOpen.Point3d(-201.72167163084575, 32.427207236186717, -6.3475734329472289)
    constraintReference1.HelpPoint = helpPoint1
    
    component3 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 3 3")
    face3 = component3.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 120 {(0,0,0) EXTRUDE(1)}")
    constraintReference2 = componentConstraint1.CreateConstraintReference(component3, face3, False, False, False)
    
    helpPoint2 = NXOpen.Point3d(-16.661086561672857, 126.71309441773474, 6.3586976677070242)
    constraintReference2.HelpPoint = helpPoint2
    
    constraintReference2.SetFixHint(True)
    
    componentConstraint1.SetAlignmentHint(NXOpen.Positioning.Constraint.Alignment.ContraAlign)
    
    componentNetwork2.Solve()
    
    scaleAboutPoint15 = NXOpen.Point3d(-22.351246859527201, -24.524284748647638, 0.0)
    viewCenter15 = NXOpen.Point3d(22.351246859527016, 24.524284748648011, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(-26.968952373908689, -27.551016094208578, 0.0)
    viewCenter16 = NXOpen.Point3d(26.96895237390849, 27.551016094208972, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(-33.711190467385819, -34.438770117760761, 0.0)
    viewCenter17 = NXOpen.Point3d(33.711190467385649, 34.438770117761152, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(-42.138988084232224, -43.048462647201006, 0.0)
    viewCenter18 = NXOpen.Point3d(42.138988084232118, 43.04846264720139, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(-52.673735105290284, -53.810578309001322, 0.0)
    viewCenter19 = NXOpen.Point3d(52.673735105290156, 53.810578309001713, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint19, viewCenter19)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = -0.51581055336333281
    rotMatrix2.Xy = 0.61613501977845386
    rotMatrix2.Xz = -0.59524542034492955
    rotMatrix2.Yx = -0.85573209413056739
    rotMatrix2.Yy = -0.33748308456065462
    rotMatrix2.Yz = 0.39220881008760261
    rotMatrix2.Zx = 0.040768322431999876
    rotMatrix2.Zy = 0.71167605343865747
    rotMatrix2.Zz = 0.70132384734019204
    translation2 = NXOpen.Point3d(-149.43474687516155, -35.644304561500547, -286.82237709744305)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.5585642751146338)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "復原上一個約束")
    
    componentConstraint1.FlipAlignment()
    
    componentNetwork2.Solve()
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId5)
    
    componentNetwork2.Solve()
    
    componentPositioner2.ClearNetwork()
    
    nErrs3 = theSession.UpdateManager.AddToDeleteList(componentNetwork2)
    
    componentPositioner2.DeleteNonPersistentConstraints()
    
    nErrs4 = theSession.UpdateManager.DoUpdate(markId5)
    
    theSession.DeleteUndoMark(markId8, None)
    
    theSession.SetUndoMarkName(markId4, "組立約束")
    
    componentPositioner2.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner2.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId5, None)
    
    theSession.DeleteUndoMark(markId7, None)
    
    theSession.DeleteUndoMark(markId6, None)
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner3 = workPart.ComponentAssembly.Positioner
    
    componentPositioner3.ClearNetwork()
    
    componentPositioner3.PrimaryArrangement = arrangement1
    
    componentPositioner3.BeginAssemblyConstraints()
    
    allowInterpartPositioning3 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network3 = componentPositioner3.EstablishNetwork()
    
    componentNetwork3 = network3
    componentNetwork3.MoveObjectsState = True
    
    componentNetwork3.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork3.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId9, "組立約束 對話方塊")
    
    componentNetwork3.MoveObjectsState = True
    
    componentNetwork3.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = -0.16971700813244833
    rotMatrix3.Xy = 0.047236914240045218
    rotMatrix3.Xz = -0.98436010234245308
    rotMatrix3.Yx = -0.62484848244499369
    rotMatrix3.Yy = -0.77756384438026016
    rotMatrix3.Yz = 0.070419045000464003
    rotMatrix3.Zx = -0.7620764470423913
    rotMatrix3.Zy = 0.62702722576110281
    rotMatrix3.Zz = 0.16148172347845854
    translation3 = NXOpen.Point3d(-91.384558491010367, 7.2964643865316017, -323.74929669823223)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 0.5585642751146338)
    
    scaleAboutPoint20 = NXOpen.Point3d(-74.36849290944761, 2.842108009278451, 0.0)
    viewCenter20 = NXOpen.Point3d(74.36849290944744, -2.8421080092780469, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(-59.873742062128535, 2.2736864074227934, 0.0)
    viewCenter21 = NXOpen.Point3d(59.873742062128407, -2.2736864074224052, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(-47.898993649702824, 1.8189491259382859, 0.0)
    viewCenter22 = NXOpen.Point3d(47.898993649702717, -1.8189491259378983, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(-38.319194919762261, 1.4551593007506496, 0.0)
    viewCenter23 = NXOpen.Point3d(38.319194919762161, -1.4551593007502774, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint23, viewCenter23)
    
    face4 = component2.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 150 {(0,-7.5,-5) EXTRUDE(1)}")
    line2 = workPart.Lines.CreateFaceAxis(face4, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects2 = [NXOpen.TaggedObject.Null] * 1 
    objects2[0] = line2
    nErrs5 = theSession.UpdateManager.AddObjectsToDeleteList(objects2)
    
    scaleAboutPoint24 = NXOpen.Point3d(-40.356417940812925, -10.089104485203038, 0.0)
    viewCenter24 = NXOpen.Point3d(40.35641794081279, 10.0891044852034, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(-50.445522426016119, -12.853907156628923, 0.0)
    viewCenter25 = NXOpen.Point3d(50.445522426016012, 12.853907156629294, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint25, viewCenter25)
    
    scaleAboutPoint26 = NXOpen.Point3d(-63.360061220176497, -16.976858508755218, 0.0)
    viewCenter26 = NXOpen.Point3d(63.360061220176391, 16.97685850875563, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(-82.231658401784088, -84.884292543776866, 0.0)
    viewCenter27 = NXOpen.Point3d(82.23165840178396, 84.884292543777249, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(-66.997959472052656, -70.635857723928552, 0.0)
    viewCenter28 = NXOpen.Point3d(66.997959472052557, 70.635857723928964, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint28, viewCenter28)
    
    scaleAboutPoint29 = NXOpen.Point3d(-54.325947228017363, -59.176478230518669, 0.0)
    viewCenter29 = NXOpen.Point3d(54.325947228017256, 59.176478230519024, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(-43.848800262614006, -48.117267544815171, 0.0)
    viewCenter30 = NXOpen.Point3d(43.848800262613935, 48.117267544815519, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint30, viewCenter30)
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint2 = componentPositioner3.CreateConstraint(True)
    
    componentConstraint2 = constraint2
    componentConstraint2.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge1 = component2.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 120 * 150 {(-2.5,0,4.3301270189222)(5,0,-0)(-2.5,0,-4.3301270189222) EXTRUDE(1)}")
    constraintReference3 = componentConstraint2.CreateConstraintReference(component2, edge1, False, False, False)
    
    helpPoint3 = NXOpen.Point3d(-16.66108656167286, 29.122062169686298, -3.6558431035319976)
    constraintReference3.HelpPoint = helpPoint3
    
    edge2 = component3.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 120 * 140 {(0,-2.5000000000001,4.3301270189223)(0,5.0000000000001,-0)(0,-2.5000000000001,-4.3301270189223) EXTRUDE(1)}")
    constraintReference4 = componentConstraint2.CreateConstraintReference(component3, edge2, False, False, False)
    
    helpPoint4 = NXOpen.Point3d(-16.661086561672857, 124.19467077775734, 10.962501798722212)
    constraintReference4.HelpPoint = helpPoint4
    
    constraintReference4.SetFixHint(True)
    
    componentNetwork3.Solve()
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs6 = theSession.UpdateManager.DoUpdate(markId10)
    
    componentNetwork3.Solve()
    
    componentPositioner3.ClearNetwork()
    
    nErrs7 = theSession.UpdateManager.AddToDeleteList(componentNetwork3)
    
    componentPositioner3.DeleteNonPersistentConstraints()
    
    nErrs8 = theSession.UpdateManager.DoUpdate(markId10)
    
    theSession.DeleteUndoMark(markId12, None)
    
    theSession.SetUndoMarkName(markId9, "組立約束")
    
    componentPositioner3.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner3.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId10, None)
    
    theSession.DeleteUndoMark(markId11, None)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner4 = workPart.ComponentAssembly.Positioner
    
    componentPositioner4.ClearNetwork()
    
    componentPositioner4.PrimaryArrangement = arrangement1
    
    componentPositioner4.BeginAssemblyConstraints()
    
    allowInterpartPositioning4 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression33 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression34 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression35 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression36 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression37 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network4 = componentPositioner4.EstablishNetwork()
    
    componentNetwork4 = network4
    componentNetwork4.MoveObjectsState = True
    
    componentNetwork4.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork4.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId13, "組立約束 對話方塊")
    
    componentNetwork4.MoveObjectsState = True
    
    componentNetwork4.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    scaleAboutPoint31 = NXOpen.Point3d(-62.552447808259963, 1.7204975765485895e-13, 0.0)
    viewCenter31 = NXOpen.Point3d(62.552447808259885, 1.7204975765485895e-13, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(-64.60907295332062, -1.7461911609003911, 0.0)
    viewCenter32 = NXOpen.Point3d(64.609072953320521, 1.7461911609007386, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(-60.389110981144285, -4.1229513521261625, 0.0)
    viewCenter33 = NXOpen.Point3d(60.389110981144185, 4.1229513521265142, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint33, viewCenter33)
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = -0.40031514034317961
    rotMatrix4.Xy = 0.29195276829387745
    rotMatrix4.Xz = -0.86862613908260689
    rotMatrix4.Yx = -0.81317355275526604
    rotMatrix4.Yy = -0.5501922309061914
    rotMatrix4.Yz = 0.18983488127802892
    rotMatrix4.Zx = -0.42248853417742971
    rotMatrix4.Zy = 0.7823375806747388
    rotMatrix4.Zz = 0.45765854996120664
    translation4 = NXOpen.Point3d(-113.07043181470473, 20.405908577049924, -316.66322235007743)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 0.87275667986661531)
    
    scaleAboutPoint34 = NXOpen.Point3d(-75.486388726430363, 38.804248020012551, 0.0)
    viewCenter34 = NXOpen.Point3d(75.486388726430249, -38.804248020012189, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint34, viewCenter34)
    
    scaleAboutPoint35 = NXOpen.Point3d(-93.600090438897084, 49.642153228726919, 0.0)
    viewCenter35 = NXOpen.Point3d(93.600090438896956, -49.642153228726599, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(-117.00011304862134, 62.0526915359086, 0.0)
    viewCenter36 = NXOpen.Point3d(117.00011304862117, -62.052691535908281, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(-103.02641533633663, 190.06597312048311, 0.0)
    viewCenter37 = NXOpen.Point3d(103.02641533633643, -190.06597312048279, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint37, viewCenter37)
    
    scaleAboutPoint38 = NXOpen.Point3d(-81.000078264430172, 152.05277849638645, 0.0)
    viewCenter38 = NXOpen.Point3d(81.000078264430016, -152.05277849638617, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(-63.284271673262431, 121.64222279710916, 0.0)
    viewCenter39 = NXOpen.Point3d(63.284271673262303, -121.6422227971089, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint39, viewCenter39)
    
    scaleAboutPoint40 = NXOpen.Point3d(-48.808468212671862, 96.707461862374714, 0.0)
    viewCenter40 = NXOpen.Point3d(48.808468212671812, -96.707461862374402, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint40, viewCenter40)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint3 = componentPositioner4.CreateConstraint(True)
    
    componentConstraint3 = constraint3
    componentConstraint3.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.InferAlign
    
    componentConstraint3.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    component4 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 2 2")
    face5 = component4.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 120 {(0,0,0) EXTRUDE(1)}")
    constraintReference5 = componentConstraint3.CreateConstraintReference(component4, face5, False, False, False)
    
    helpPoint5 = NXOpen.Point3d(-166.57844310584005, 32.427207236186717, -3.8907756679691374)
    constraintReference5.HelpPoint = helpPoint5
    
    component5 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 3 1")
    face6 = component5.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 120 {(0,0,0) EXTRUDE(1)}")
    constraintReference6 = componentConstraint3.CreateConstraintReference(component5, face6, False, False, False)
    
    helpPoint6 = NXOpen.Point3d(-16.661086561672857, 45.101305492219183, 11.969008896367084)
    constraintReference6.HelpPoint = helpPoint6
    
    constraintReference6.SetFixHint(True)
    
    componentConstraint3.SetAlignmentHint(NXOpen.Positioning.Constraint.Alignment.ContraAlign)
    
    componentNetwork4.Solve()
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "復原上一個約束")
    
    componentConstraint3.FlipAlignment()
    
    componentNetwork4.Solve()
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs9 = theSession.UpdateManager.DoUpdate(markId14)
    
    componentNetwork4.Solve()
    
    componentPositioner4.ClearNetwork()
    
    nErrs10 = theSession.UpdateManager.AddToDeleteList(componentNetwork4)
    
    componentPositioner4.DeleteNonPersistentConstraints()
    
    nErrs11 = theSession.UpdateManager.DoUpdate(markId14)
    
    theSession.DeleteUndoMark(markId17, None)
    
    theSession.SetUndoMarkName(markId13, "組立約束")
    
    componentPositioner4.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner4.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId14, None)
    
    theSession.DeleteUndoMark(markId16, None)
    
    theSession.DeleteUndoMark(markId15, None)
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner5 = workPart.ComponentAssembly.Positioner
    
    componentPositioner5.ClearNetwork()
    
    componentPositioner5.PrimaryArrangement = arrangement1
    
    componentPositioner5.BeginAssemblyConstraints()
    
    allowInterpartPositioning5 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression38 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression39 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression40 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression41 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression42 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression43 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression44 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression45 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network5 = componentPositioner5.EstablishNetwork()
    
    componentNetwork5 = network5
    componentNetwork5.MoveObjectsState = True
    
    componentNetwork5.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork5.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId18, "組立約束 對話方塊")
    
    componentNetwork5.MoveObjectsState = True
    
    componentNetwork5.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    face7 = component4.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 140 {(0,-7.5,-9.9999999999994) EXTRUDE(1)}")
    line3 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face8 = component4.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 150 {(0,-7.5,-5) EXTRUDE(1)}")
    line4 = workPart.Lines.CreateFaceAxis(face8, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    objects3[0] = line3
    nErrs12 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    objects4 = [NXOpen.TaggedObject.Null] * 1 
    objects4[0] = line4
    nErrs13 = theSession.UpdateManager.AddObjectsToDeleteList(objects4)
    
    face9 = component5.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 140 {(20,0,-5.0000000000001) EXTRUDE(1)}")
    line5 = workPart.Lines.CreateFaceAxis(face9, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line6 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint4 = componentPositioner5.CreateConstraint(True)
    
    componentConstraint4 = constraint4
    componentConstraint4.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge3 = component4.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 120 * 150 {(-2.5,0,4.3301270189222)(5,0,-0)(-2.5,0,-4.3301270189222) EXTRUDE(1)}")
    constraintReference7 = componentConstraint4.CreateConstraintReference(component4, edge3, False, False, False)
    
    helpPoint7 = NXOpen.Point3d(-16.66108656167286, 27.660563500918379, 1.4041709099746398)
    constraintReference7.HelpPoint = helpPoint7
    
    edge4 = component5.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 120 * 140 {(0,-2.5000000000001,4.3301270189223)(0,5.0000000000001,-0)(0,-2.5000000000001,-4.3301270189223) EXTRUDE(1)}")
    constraintReference8 = componentConstraint4.CreateConstraintReference(component5, edge4, False, False, False)
    
    helpPoint8 = NXOpen.Point3d(-16.661086561672857, 45.453798876585402, 14.95784229929718)
    constraintReference8.HelpPoint = helpPoint8
    
    constraintReference8.SetFixHint(True)
    
    objects5 = [NXOpen.TaggedObject.Null] * 1 
    objects5[0] = line5
    nErrs14 = theSession.UpdateManager.AddObjectsToDeleteList(objects5)
    
    objects6 = [NXOpen.TaggedObject.Null] * 1 
    objects6[0] = line6
    nErrs15 = theSession.UpdateManager.AddObjectsToDeleteList(objects6)
    
    componentNetwork5.Solve()
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs16 = theSession.UpdateManager.DoUpdate(markId19)
    
    componentNetwork5.Solve()
    
    componentPositioner5.ClearNetwork()
    
    nErrs17 = theSession.UpdateManager.AddToDeleteList(componentNetwork5)
    
    componentPositioner5.DeleteNonPersistentConstraints()
    
    nErrs18 = theSession.UpdateManager.DoUpdate(markId19)
    
    theSession.DeleteUndoMark(markId21, None)
    
    theSession.SetUndoMarkName(markId18, "組立約束")
    
    componentPositioner5.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner5.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId19, None)
    
    theSession.DeleteUndoMark(markId20, None)
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner6 = workPart.ComponentAssembly.Positioner
    
    componentPositioner6.ClearNetwork()
    
    componentPositioner6.PrimaryArrangement = arrangement1
    
    componentPositioner6.BeginAssemblyConstraints()
    
    allowInterpartPositioning6 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression46 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression47 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression48 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression49 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression50 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression51 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression52 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression53 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network6 = componentPositioner6.EstablishNetwork()
    
    componentNetwork6 = network6
    componentNetwork6.MoveObjectsState = True
    
    componentNetwork6.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork6.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId22, "組立約束 對話方塊")
    
    componentNetwork6.MoveObjectsState = True
    
    componentNetwork6.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    scaleAboutPoint41 = NXOpen.Point3d(-73.24301813777339, 7.0332699536273786, 0.0)
    viewCenter41 = NXOpen.Point3d(73.243018137773305, -7.0332699536270891, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint41, viewCenter41)
    
    scaleAboutPoint42 = NXOpen.Point3d(-92.766405422842098, 7.2757965037524723, 0.0)
    viewCenter42 = NXOpen.Point3d(92.766405422842041, -7.2757965037521615, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint42, viewCenter42)
    
    scaleAboutPoint43 = NXOpen.Point3d(-116.71590224769352, 7.9579024259792588, 0.0)
    viewCenter43 = NXOpen.Point3d(116.71590224769339, -7.9579024259789364, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(-145.89487780961687, 9.947378032473992, 0.0)
    viewCenter44 = NXOpen.Point3d(145.89487780961673, -9.9473780324737096, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(-193.61860813208071, -26.644762586983433, 0.0)
    viewCenter45 = NXOpen.Point3d(193.61860813208071, 26.644762586983685, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint45, viewCenter45)
    
    scaleAboutPoint46 = NXOpen.Point3d(-247.94431851776395, -40.707276174558082, 0.0)
    viewCenter46 = NXOpen.Point3d(247.94431851776395, 40.707276174558466, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint46, viewCenter46)
    
    scaleAboutPoint47 = NXOpen.Point3d(-313.6310596176192, -56.435087423819255, 0.0)
    viewCenter47 = NXOpen.Point3d(313.6310596176192, 56.435087423819652, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint47, viewCenter47)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = -0.17830110437426233
    rotMatrix5.Xy = 0.94314361560225202
    rotMatrix5.Xz = -0.28051530533578051
    rotMatrix5.Yx = 0.19184963774357564
    rotMatrix5.Yy = 0.31293373843123062
    rotMatrix5.Yz = 0.93019685650355932
    rotMatrix5.Zx = 0.96509192965052171
    rotMatrix5.Zy = 0.11203836708985274
    rotMatrix5.Zz = -0.23673819215171499
    translation5 = NXOpen.Point3d(-454.93078437758356, -79.79891147626833, -187.24012727247592)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 0.22878792708695406)
    
    scaleAboutPoint48 = NXOpen.Point3d(-351.56283968936663, -42.788898251666176, 0.0)
    viewCenter48 = NXOpen.Point3d(351.5628396893668, 42.788898251666573, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(-284.9509332219078, -39.78211080695452, 0.0)
    viewCenter49 = NXOpen.Point3d(284.9509332219078, 39.782110806954911, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint49, viewCenter49)
    
    scaleAboutPoint50 = NXOpen.Point3d(-230.18114345977489, -37.006614704143722, 0.0)
    viewCenter50 = NXOpen.Point3d(230.18114345977489, 37.006614704144098, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint50, viewCenter50)
    
    scaleAboutPoint51 = NXOpen.Point3d(-184.14491476781987, -29.605291763314924, 0.0)
    viewCenter51 = NXOpen.Point3d(184.14491476781996, 29.605291763315329, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(-147.3159318142558, -24.157918078864913, 0.0)
    viewCenter52 = NXOpen.Point3d(147.315931814256, 24.157918078865318, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint52, viewCenter52)
    
    scaleAboutPoint53 = NXOpen.Point3d(-101.93694059944643, 12.884222975394918, 0.0)
    viewCenter53 = NXOpen.Point3d(101.93694059944669, -12.884222975394531, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(-80.94323610424442, 11.823169318597722, 0.0)
    viewCenter54 = NXOpen.Point3d(80.943236104244676, -11.823169318597309, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint54, viewCenter54)
    
    scaleAboutPoint55 = NXOpen.Point3d(-64.754588883395527, 9.4585354548782181, 0.0)
    viewCenter55 = NXOpen.Point3d(64.754588883395741, -9.4585354548778042, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(-51.803671106716415, 7.5668283639026255, 0.0)
    viewCenter56 = NXOpen.Point3d(51.803671106716585, -7.5668283639021947, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint56, viewCenter56)
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint5 = componentPositioner6.CreateConstraint(True)
    
    componentConstraint5 = constraint5
    componentConstraint5.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.InferAlign
    
    componentConstraint5.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    face10 = component1.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 120 {(0,0,0) EXTRUDE(1)}")
    constraintReference9 = componentConstraint5.CreateConstraintReference(component1, face10, False, False, False)
    
    helpPoint9 = NXOpen.Point3d(-150.84440500825397, 1.9282318435621306, 0.66442169088531955)
    constraintReference9.HelpPoint = helpPoint9
    
    component6 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 3 4")
    face11 = component6.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 120 {(0,0,0) EXTRUDE(1)}")
    constraintReference10 = componentConstraint5.CreateConstraintReference(component6, face11, False, False, False)
    
    helpPoint10 = NXOpen.Point3d(73.338913438327154, 123.09869339217039, 7.4596901995239593)
    constraintReference10.HelpPoint = helpPoint10
    
    constraintReference10.SetFixHint(True)
    
    componentConstraint5.SetAlignmentHint(NXOpen.Positioning.Constraint.Alignment.ContraAlign)
    
    componentNetwork6.Solve()
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "復原上一個約束")
    
    componentConstraint5.FlipAlignment()
    
    componentNetwork6.Solve()
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs19 = theSession.UpdateManager.DoUpdate(markId23)
    
    componentNetwork6.Solve()
    
    componentPositioner6.ClearNetwork()
    
    nErrs20 = theSession.UpdateManager.AddToDeleteList(componentNetwork6)
    
    componentPositioner6.DeleteNonPersistentConstraints()
    
    nErrs21 = theSession.UpdateManager.DoUpdate(markId23)
    
    theSession.DeleteUndoMark(markId26, None)
    
    theSession.SetUndoMarkName(markId22, "組立約束")
    
    componentPositioner6.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner6.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId23, None)
    
    theSession.DeleteUndoMark(markId25, None)
    
    theSession.DeleteUndoMark(markId24, None)
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner7 = workPart.ComponentAssembly.Positioner
    
    componentPositioner7.ClearNetwork()
    
    componentPositioner7.PrimaryArrangement = arrangement1
    
    componentPositioner7.BeginAssemblyConstraints()
    
    allowInterpartPositioning7 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression54 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression55 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression56 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression57 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression58 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression59 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression60 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression61 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network7 = componentPositioner7.EstablishNetwork()
    
    componentNetwork7 = network7
    componentNetwork7.MoveObjectsState = True
    
    componentNetwork7.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork7.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId27, "組立約束 對話方塊")
    
    componentNetwork7.MoveObjectsState = True
    
    componentNetwork7.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    scaleAboutPoint57 = NXOpen.Point3d(-76.366760103384237, 7.2951986277625434, 0.0)
    viewCenter57 = NXOpen.Point3d(76.366760103384365, -7.2951986277621073, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(-111.17417057733532, 17.849954089205891, 0.0)
    viewCenter58 = NXOpen.Point3d(111.17417057733546, -17.849954089205461, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(-138.96771322166913, 22.312442611507301, 0.0)
    viewCenter59 = NXOpen.Point3d(138.9677132216693, -22.312442611506867, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint59, viewCenter59)
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = 0.47120862022415771
    rotMatrix6.Xy = 0.81002988043997515
    rotMatrix6.Xz = -0.34901866571982199
    rotMatrix6.Yx = 0.0036853318433293474
    rotMatrix6.Yy = 0.3938914025819315
    rotMatrix6.Yz = 0.91914959680198038
    rotMatrix6.Zx = 0.88201408977161422
    rotMatrix6.Zy = -0.43439746289134573
    rotMatrix6.Zz = 0.18261979541635659
    translation6 = NXOpen.Point3d(-190.39712701341688, -57.507660893503839, -161.54046137311985)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 0.87275667986661531)
    
    scaleAboutPoint60 = NXOpen.Point3d(-140.05908269723201, -1.8189491259378723, 0.0)
    viewCenter60 = NXOpen.Point3d(140.05908269723216, 1.8189491259383117, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(-175.83174884068092, -9.8526410988310573, 0.0)
    viewCenter61 = NXOpen.Point3d(175.83174884068109, 9.8526410988315103, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint61, viewCenter61)
    
    line7 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scaleAboutPoint62 = NXOpen.Point3d(-231.63180275617717, -54.947421512712594, 0.0)
    viewCenter62 = NXOpen.Point3d(231.63180275617742, 54.947421512713085, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(-185.30544220494173, -43.57898947559957, 0.0)
    viewCenter63 = NXOpen.Point3d(185.30544220494198, 43.578989475600089, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(-147.94119557629702, -34.256875205166921, 0.0)
    viewCenter64 = NXOpen.Point3d(147.94119557629728, 34.256875205167432, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(-118.1104299109125, -27.405500164133475, 0.0)
    viewCenter65 = NXOpen.Point3d(118.11042991091276, 27.40550016413399, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint65, viewCenter65)
    
    objects7 = [NXOpen.TaggedObject.Null] * 1 
    objects7[0] = line7
    nErrs22 = theSession.UpdateManager.AddObjectsToDeleteList(objects7)
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint6 = componentPositioner7.CreateConstraint(True)
    
    componentConstraint6 = constraint6
    componentConstraint6.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge5 = component1.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 120 * 150 {(-2.5,0,4.3301270189222)(5,0,-0)(-2.5,0,-4.3301270189222) EXTRUDE(1)}")
    constraintReference11 = componentConstraint6.CreateConstraintReference(component1, edge5, False, False, False)
    
    helpPoint11 = NXOpen.Point3d(73.33891343832714, 6.6630197807832321, 1.7914390023182454)
    constraintReference11.HelpPoint = helpPoint11
    
    edge6 = component6.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 120 * 140 {(0,-2.5000000000001,4.3301270189223)(0,5.0000000000001,-0)(0,-2.5000000000001,-4.3301270189223) EXTRUDE(1)}")
    constraintReference12 = componentConstraint6.CreateConstraintReference(component6, edge6, False, False, False)
    
    helpPoint12 = NXOpen.Point3d(73.338913438327154, 128.99379019044144, 8.7315568176264904)
    constraintReference12.HelpPoint = helpPoint12
    
    constraintReference12.SetFixHint(True)
    
    componentNetwork7.Solve()
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs23 = theSession.UpdateManager.DoUpdate(markId28)
    
    componentNetwork7.Solve()
    
    componentPositioner7.ClearNetwork()
    
    nErrs24 = theSession.UpdateManager.AddToDeleteList(componentNetwork7)
    
    componentPositioner7.DeleteNonPersistentConstraints()
    
    nErrs25 = theSession.UpdateManager.DoUpdate(markId28)
    
    theSession.DeleteUndoMark(markId30, None)
    
    theSession.SetUndoMarkName(markId27, "組立約束")
    
    componentPositioner7.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner7.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId28, None)
    
    theSession.DeleteUndoMark(markId29, None)
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner8 = workPart.ComponentAssembly.Positioner
    
    componentPositioner8.ClearNetwork()
    
    componentPositioner8.PrimaryArrangement = arrangement1
    
    componentPositioner8.BeginAssemblyConstraints()
    
    allowInterpartPositioning8 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression62 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression63 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression64 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression65 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression66 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression67 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression68 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression69 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network8 = componentPositioner8.EstablishNetwork()
    
    componentNetwork8 = network8
    componentNetwork8.MoveObjectsState = True
    
    componentNetwork8.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork8.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId31, "組立約束 對話方塊")
    
    componentNetwork8.MoveObjectsState = True
    
    componentNetwork8.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    scaleAboutPoint66 = NXOpen.Point3d(-136.20291055024327, -19.208102769905853, 0.0)
    viewCenter66 = NXOpen.Point3d(136.2029105502435, 19.208102769906365, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(-88.318468493548039, -22.351246859526871, 0.0)
    viewCenter67 = NXOpen.Point3d(88.318468493548281, 22.351246859527375, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(-70.406427607510324, -17.880997487621432, 0.0)
    viewCenter68 = NXOpen.Point3d(70.406427607510551, 17.880997487621954, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(-56.126464336145773, -14.304797990097104, 0.0)
    viewCenter69 = NXOpen.Point3d(56.126464336145993, 14.304797990097612, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint69, viewCenter69)
    
    scaleAboutPoint70 = NXOpen.Point3d(-44.821700368971619, -11.443838392077629, 0.0)
    viewCenter70 = NXOpen.Point3d(44.821700368971847, 11.443838392078137, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(-56.027125461214538, -14.304797990097104, 0.0)
    viewCenter71 = NXOpen.Point3d(56.027125461214759, 14.304797990097612, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint71, viewCenter71)
    
    scaleAboutPoint72 = NXOpen.Point3d(-70.033906826518191, -17.880997487621443, 0.0)
    viewCenter72 = NXOpen.Point3d(70.033906826518418, 17.88099748762194, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(-87.387166541067728, -21.885595883286719, 0.0)
    viewCenter73 = NXOpen.Point3d(87.38716654106797, 21.88559588328722, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint73, viewCenter73)
    
    scaleAboutPoint74 = NXOpen.Point3d(-108.0698307357343, -25.028739972907719, 0.0)
    viewCenter74 = NXOpen.Point3d(108.06983073573453, 25.028739972908198, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint74, viewCenter74)
    
    scaleAboutPoint75 = NXOpen.Point3d(-135.08728841966791, -31.285924966134708, 0.0)
    viewCenter75 = NXOpen.Point3d(135.08728841966808, 31.285924966135205, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(-168.85911052458491, -39.10740620766844, 0.0)
    viewCenter76 = NXOpen.Point3d(168.85911052458508, 39.10740620766893, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint76, viewCenter76)
    
    rotMatrix7 = NXOpen.Matrix3x3()
    
    rotMatrix7.Xx = 0.8212520737366239
    rotMatrix7.Xy = -0.51598288537649217
    rotMatrix7.Xz = 0.24352965606234325
    rotMatrix7.Yx = 0.095844611343547048
    rotMatrix7.Yy = 0.54551444101534985
    rotMatrix7.Yz = 0.83260302973272571
    rotMatrix7.Zx = -0.56245785785220981
    rotMatrix7.Zy = -0.66043595953147283
    rotMatrix7.Zz = 0.49745904504596322
    translation7 = NXOpen.Point3d(-132.97189454425865, -57.111689834627931, -234.54567763927491)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation7, 0.6982053438932927)
    
    scaleAboutPoint77 = NXOpen.Point3d(-263.36867552645083, -72.757965037522894, 0.0)
    viewCenter77 = NXOpen.Point3d(263.36867552645111, 72.757965037523405, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(-210.99809860881706, -59.722162968300019, 0.0)
    viewCenter78 = NXOpen.Point3d(210.99809860881726, 59.722162968300537, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint78, viewCenter78)
    
    scaleAboutPoint79 = NXOpen.Point3d(-169.04100543717871, -48.747836575140255, 0.0)
    viewCenter79 = NXOpen.Point3d(169.04100543717894, 48.747836575140788, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint79, viewCenter79)
    
    scaleAboutPoint80 = NXOpen.Point3d(-97.010620050030738, -29.297207255109051, 0.0)
    viewCenter80 = NXOpen.Point3d(97.010620050031036, 29.297207255109594, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint80, viewCenter80)
    
    scaleAboutPoint81 = NXOpen.Point3d(-120.53569541216321, -36.378982518761312, 0.0)
    viewCenter81 = NXOpen.Point3d(120.53569541216358, 36.378982518761852, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint81, viewCenter81)
    
    scaleAboutPoint82 = NXOpen.Point3d(-150.06330288989136, -45.170569960795362, 0.0)
    viewCenter82 = NXOpen.Point3d(150.06330288989167, 45.170569960795902, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint82, viewCenter82)
    
    rotMatrix8 = NXOpen.Matrix3x3()
    
    rotMatrix8.Xx = 0.61138550341679176
    rotMatrix8.Xy = 0.65308056957466032
    rotMatrix8.Xz = -0.44687082681220558
    rotMatrix8.Yx = 0.039832480080300242
    rotMatrix8.Yy = 0.53859256096429631
    rotMatrix8.Yz = 0.8416242788825492
    rotMatrix8.Zx = 0.79032976645349806
    rotMatrix8.Zy = -0.53235685673986699
    rotMatrix8.Zz = 0.30327386524328209
    translation8 = NXOpen.Point3d(-174.43394376945531, -51.491840100374247, -161.96381000005147)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation8, 0.6982053438932927)
    
    component7 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 3 2")
    face12 = component7.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 140 {(20,0,-5.0000000000001) EXTRUDE(1)}")
    line8 = workPart.Lines.CreateFaceAxis(face12, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line8.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint83 = NXOpen.Point3d(-106.48431341429158, -23.115811808796174, 0.0)
    viewCenter83 = NXOpen.Point3d(106.48431341429189, 23.115811808796693, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint83, viewCenter83)
    
    scaleAboutPoint84 = NXOpen.Point3d(-78.214812415337235, -15.461067570473412, 0.0)
    viewCenter84 = NXOpen.Point3d(78.214812415337548, 15.461067570473929, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint84, viewCenter84)
    
    scaleAboutPoint85 = NXOpen.Point3d(-62.571849932269735, -12.36885405637867, 0.0)
    viewCenter85 = NXOpen.Point3d(62.571849932270084, 12.368854056379186, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint85, viewCenter85)
    
    scaleAboutPoint86 = NXOpen.Point3d(-49.66943746561563, -9.8950832451028852, 0.0)
    viewCenter86 = NXOpen.Point3d(49.66943746561595, 9.8950832451033985, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint86, viewCenter86)
    
    scaleAboutPoint87 = NXOpen.Point3d(-39.58033298041245, -7.9160665960822678, 0.0)
    viewCenter87 = NXOpen.Point3d(39.580332980412742, 7.9160665960827705, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint87, viewCenter87)
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint7 = componentPositioner8.CreateConstraint(True)
    
    componentConstraint7 = constraint7
    componentConstraint7.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.InferAlign
    
    componentConstraint7.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    component8 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 2 4")
    face13 = component8.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 130 {(0,-15,0) EXTRUDE(1)}")
    constraintReference13 = componentConstraint7.CreateConstraintReference(component8, face13, False, False, False)
    
    helpPoint13 = NXOpen.Point3d(-172.48424242346618, -13.071768156537914, 0.35044029641539964)
    constraintReference13.HelpPoint = helpPoint13
    
    face14 = component7.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 120 {(0,0,0) EXTRUDE(1)}")
    constraintReference14 = componentConstraint7.CreateConstraintReference(component7, face14, False, False, False)
    
    helpPoint14 = NXOpen.Point3d(73.338913438327154, 44.923292707620803, 8.7869707663775447)
    constraintReference14.HelpPoint = helpPoint14
    
    constraintReference14.SetFixHint(True)
    
    componentConstraint7.SetAlignmentHint(NXOpen.Positioning.Constraint.Alignment.ContraAlign)
    
    objects8 = [NXOpen.TaggedObject.Null] * 1 
    objects8[0] = line8
    nErrs26 = theSession.UpdateManager.AddObjectsToDeleteList(objects8)
    
    componentNetwork8.Solve()
    
    scaleAboutPoint88 = NXOpen.Point3d(-35.513647787915161, -4.3460757782411354, 0.0)
    viewCenter88 = NXOpen.Point3d(35.513647787915438, 4.3460757782416328, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint88, viewCenter88)
    
    scaleAboutPoint89 = NXOpen.Point3d(-44.54727672697404, -5.4325947228014977, 0.0)
    viewCenter89 = NXOpen.Point3d(44.547276726974303, 5.432594722801988, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint89, viewCenter89)
    
    scaleAboutPoint90 = NXOpen.Point3d(-55.684095908717595, -6.9847646436019737, 0.0)
    viewCenter90 = NXOpen.Point3d(55.684095908717858, 6.9847646436024533, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint90, viewCenter90)
    
    line9 = workPart.Lines.CreateFaceAxis(face12, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line9.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "復原上一個約束")
    
    componentConstraint7.FlipAlignment()
    
    objects9 = [NXOpen.TaggedObject.Null] * 1 
    objects9[0] = line9
    nErrs27 = theSession.UpdateManager.AddObjectsToDeleteList(objects9)
    
    componentNetwork8.Solve()
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs28 = theSession.UpdateManager.DoUpdate(markId32)
    
    componentNetwork8.Solve()
    
    componentPositioner8.ClearNetwork()
    
    nErrs29 = theSession.UpdateManager.AddToDeleteList(componentNetwork8)
    
    componentPositioner8.DeleteNonPersistentConstraints()
    
    nErrs30 = theSession.UpdateManager.DoUpdate(markId32)
    
    theSession.DeleteUndoMark(markId35, None)
    
    theSession.SetUndoMarkName(markId31, "組立約束")
    
    componentPositioner8.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner8.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId32, None)
    
    theSession.DeleteUndoMark(markId34, None)
    
    theSession.DeleteUndoMark(markId33, None)
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner9 = workPart.ComponentAssembly.Positioner
    
    componentPositioner9.ClearNetwork()
    
    componentPositioner9.PrimaryArrangement = arrangement1
    
    componentPositioner9.BeginAssemblyConstraints()
    
    allowInterpartPositioning9 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression70 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression71 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression72 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression73 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression74 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression75 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression76 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression77 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network9 = componentPositioner9.EstablishNetwork()
    
    componentNetwork9 = network9
    componentNetwork9.MoveObjectsState = True
    
    componentNetwork9.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork9.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId36, "組立約束 對話方塊")
    
    componentNetwork9.MoveObjectsState = True
    
    componentNetwork9.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    face15 = component8.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 140 {(0,-7.5,-9.9999999999994) EXTRUDE(1)}")
    line10 = workPart.Lines.CreateFaceAxis(face15, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    face16 = component8.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 150 {(0,-7.5,-5) EXTRUDE(1)}")
    line11 = workPart.Lines.CreateFaceAxis(face16, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects10 = [NXOpen.TaggedObject.Null] * 1 
    objects10[0] = line10
    nErrs31 = theSession.UpdateManager.AddObjectsToDeleteList(objects10)
    
    objects11 = [NXOpen.TaggedObject.Null] * 1 
    objects11[0] = line11
    nErrs32 = theSession.UpdateManager.AddObjectsToDeleteList(objects11)
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint8 = componentPositioner9.CreateConstraint(True)
    
    componentConstraint8 = constraint8
    componentConstraint8.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge7 = component8.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 130 * 150 {(-2.5,-15,4.3301270189222)(5,-15,-0)(-2.5,-15,-4.3301270189222) EXTRUDE(1)}")
    constraintReference15 = componentConstraint8.CreateConstraintReference(component8, edge7, False, False, False)
    
    helpPoint15 = NXOpen.Point3d(73.338913438327168, -8.390733601094416, -1.8253250412102489)
    constraintReference15.HelpPoint = helpPoint15
    
    edge8 = component7.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 120 * 140 {(0,-2.5000000000001,4.3301270189223)(0,5.0000000000001,-0)(0,-2.5000000000001,-4.3301270189223) EXTRUDE(1)}")
    constraintReference16 = componentConstraint8.CreateConstraintReference(component7, edge8, False, False, False)
    
    helpPoint16 = NXOpen.Point3d(73.338913438327154, 48.838654247221662, 8.9557954071794761)
    constraintReference16.HelpPoint = helpPoint16
    
    constraintReference16.SetFixHint(True)
    
    componentNetwork9.Solve()
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs33 = theSession.UpdateManager.DoUpdate(markId37)
    
    componentNetwork9.Solve()
    
    componentPositioner9.ClearNetwork()
    
    nErrs34 = theSession.UpdateManager.AddToDeleteList(componentNetwork9)
    
    componentPositioner9.DeleteNonPersistentConstraints()
    
    nErrs35 = theSession.UpdateManager.DoUpdate(markId37)
    
    theSession.DeleteUndoMark(markId39, None)
    
    theSession.SetUndoMarkName(markId36, "組立約束")
    
    componentPositioner9.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner9.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId37, None)
    
    theSession.DeleteUndoMark(markId38, None)
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner10 = workPart.ComponentAssembly.Positioner
    
    componentPositioner10.ClearNetwork()
    
    componentPositioner10.PrimaryArrangement = arrangement1
    
    componentPositioner10.BeginAssemblyConstraints()
    
    allowInterpartPositioning10 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression78 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression79 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression80 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression81 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression82 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression83 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression84 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression85 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network10 = componentPositioner10.EstablishNetwork()
    
    componentNetwork10 = network10
    componentNetwork10.MoveObjectsState = True
    
    componentNetwork10.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork10.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId40, "組立約束 對話方塊")
    
    componentNetwork10.MoveObjectsState = True
    
    componentNetwork10.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    componentPositioner10.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner10.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId41, None)
    
    theSession.UndoToMark(markId40, None)
    
    theSession.DeleteUndoMark(markId40, None)
    
    theSession.DeleteUndoMark(markId3, None)
    
    # ----------------------------------------------
    #   功能表：檔案(F)->另存新檔(A)...
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：工具(T)->動作記錄(J)->停止錄製(S)
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()